from django.shortcuts import render_to_response
from django.template import RequestContext
import logging
from instagram import subscriptions
import fromthepit.models
from fromthepit.tasks import fetch_instagram_for_tag
from django.http import HttpResponse

subs_logger = logging.getLogger('logview.subs_logs')

CONFIG = {
	'client_id': 'ff1a989e5b4949a38fcd3d32f51a59d9',
	'client_secret': '3e73e09b36074d68a04023fa5cfdae4f'
}

def instagram_sub(request):
	subs_logger.info("Received request from subscription.")
	mode         = request.GET.get('hub.mode')
	subs_logger.info("Got hub.mode value: " + mode)
	challenge    = request.GET.get('hub.challenge')
	subs_logger.info("Got hub.challenge value: " + challenge)
	#verify_token = request.GET.get('hub.verify_token')
	#subs_logger.info("Got hub.verify_token value: " + verify_token)
	if challenge:
		subs_logger.info("Sending challenge to Instagram")
		return HttpResponse(challenge)
	else:
		reactor = subscriptions.SubscriptionsReactor()
		subs_logger.info("Creating Subscription Reactor...")
		reactor.register_callback(subscriptions.SubscriptionType.TAG, parse_instagram_update)
		subs_logger.info("Registering callback from reactor...")

		x_hub_signature = request.headers.get('X-Hub-Signature')
		subs_logger.info("Getting X-Hub-Signature: "+x_hub_signature)
		raw_response    = request.body.read()
		subs_logger.info("Getting subscription JSON response"+raw_response)
		try:
			reactor.process(CONFIG['client_secret'], raw_response, x_hub_signature)
			subs_logger.info("Processing subscription...")
		except subscriptions.SubscriptionVerifyError:
			subs_logger.error('Instagram signature mismatch')
	return Response('Parsed instagram')

def parse_instagram_update(update):
	subs_logger.info("Processing update." + update)
	concert_tag = update['object_id']
	concert = models.Concert.all().filter('instagram_tag =', concert_tag)
	if len(concert) == 0:
		subs_logger.info('Didnt find matching tag for this update')
	else:
		subs_logger.debug('Fetching all the recent pictures using a Celery task')
		fetch_instagram_for_tag.delay(concert_tag, concert)