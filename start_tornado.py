import os
import tornado.httpserver
import tornado.ioloop
import tornado.wsgi
import tornado.web
import sys
import django.core.handlers.wsgi
import logging
import json
sys.path.append('') # path to your project ( if you have it in another dir).
from instagram import subscriptions
from fromthepit.tasks import *
from fromthepit.models import Concert



subs_logger = logging.getLogger('logview.subs_logs')
hdlr = logging.FileHandler('')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)d %(message)s')
hdlr.setFormatter(formatter)
subs_logger.addHandler(hdlr) 
subs_logger.setLevel(logging.DEBUG)

CONFIG = {
	'client_id': '',
	'client_secret': ''
}

def parse_instagram_update_for_tag(update):
	concert_tag = update['object_id']
	subs_logger.info("Processing update for tag: " + concert_tag)
	concert = Concert.objects.get(instagram_tag=concert_tag)
	subs_logger.info('Created concert object...')
	
	if concert is None:
		subs_logger.info('Didnt find matching tag for this update')
	else:
		if concert.subscription_id == '':
			concert.subscription_id = update['subscription_id']
			subs_logger.info('Concert object did not have the subscription_id, updating to: ' + str(update['subscription_id']))
			concert.save()
			subs_logger.info('Saving updated subscription_id to concert object: ' + concert.main_artist.name)
			
	fetch_instagram_for_tag.delay(concert_tag)
	subs_logger.debug('Fetching all the recent pictures using a Celery task...')


def parse_instagram_update_for_location(update):
	location_id = update['object_id']
	subs_logger.info("Processing update for location id: " + location_id)
	concert = Concert.objects.filter(event_info__date=date.today(), venue__foursquare_location_id=location_id)
	subs_logger.info('Created concert object...')
	if concert is None:
		subs_logger.info('Didnt find matching tag for this update')
	else:	
		fetch_instagram_for_location.delay(location_id)
		subs_logger.debug('Fetching all the recent pictures using a Celery task...')


class HelloHandler(tornado.web.RequestHandler):
	def get(self):
		print "I'm inside Hello Handler!"
		self.write('Hello from tornado')
		
class SubscriptionHandler(tornado.web.RequestHandler):
	
	def get(self):
		print 'Received request from subscription.'
		subs_logger.info("Received request from subscription.")
		mode         = self.get_argument('hub.mode')
		print 'Got hub.mode value: ' + mode
		subs_logger.info("Got hub.mode value: " + mode)
		challenge    = self.get_argument('hub.challenge')
		print 'Got hub.challenge value: ' + challenge
		subs_logger.info("Got hub.challenge value: " + challenge)
		if challenge:
			print 'Sending challenge to Instagram'
			subs_logger.info("Sending challenge to Instagram")
			return self.write(challenge)
	
	def post(self):
		reactor = subscriptions.SubscriptionsReactor()
		print 'Creating Subscription Reactor...'
		subs_logger.info("Creating Subscription Reactor...")
		raw_response    = self.request.body
		subs_logger.info('Getting subscription JSON response: '+raw_response)
		print 'Getting subscription JSON response: '+raw_response
		
		json_res = json.loads(raw_response)
		
		json_response = json_res[0]
		
		if json_response['object'] == 'tag':
			reactor.register_callback(subscriptions.SubscriptionType.TAG, parse_instagram_update_for_tag)
			print 'Registering callback from reactor for tag...'
			subs_logger.info('Registering callback from reactor for tag...')
		elif json_response['object'] == 'location':
			reactor.register_callback(subscriptions.SubscriptionType.LOCATION, parse_instagram_update_for_location)
			print 'Registering callback from reactor for location...'
			subs_logger.info('Registering callback from reactor for location...')
			
		headers = self.request.headers
		print "Getting HTTP headers..."
		subs_logger.info('Getting HTTP headers...')
		x_hub_signature = headers['X-Hub-Signature']
		subs_logger.info("Getting X-Hub-Signature: "+x_hub_signature)
		print 'Getting X-Hub-Signature: '+x_hub_signature
		try:
			reactor.process(CONFIG['client_secret'], raw_response, x_hub_signature)
			print 'Processing subscription...'
			subs_logger.info("Processing subscription...")
		except subscriptions.SubscriptionVerifyError:
			print 'Instagram signature mismatch'
			subs_logger.error('Instagram signature mismatch')
		
		return self.write('Parsed instagram')
		
def main():
	print 'Starting server...'
	os.environ['DJANGO_SETTINGS_MODULE'] = 'fromthepit.settings' # path to your settings module
	print 'Adquiring DJANGO_SETTINGS_MODULE...'
	wsgi_app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
	print 'Creating WSGI Container for Tornado...'
	tornado_app = tornado.web.Application(
		[
			(r'^/hello-tornado/$', HelloHandler),
			(r'^/sub$', SubscriptionHandler),
			('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
		]
	)
	print 'Created Tornado App for fromthepit...'
	http_server = tornado.httpserver.HTTPServer(tornado_app)
	print 'Created a http_server...'
	http_server.listen(8080)
	print 'Listening on port 8080...'
	tornado.ioloop.IOLoop.instance().start()
	print 'Starting instance... \n'

if __name__ == "__main__":
	main()

