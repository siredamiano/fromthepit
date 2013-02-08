from django.shortcuts import render_to_response
from django.template import RequestContext
import logging
from instagram import subscriptions

view_logger = logging.getLogger('logview.subs_logs')


CONFIG = {
    'client_id': 'ff1a989e5b4949a38fcd3d32f51a59d9',
    'client_secret': '3e73e09b36074d68a04023fa5cfdae4f'
}

def instagram_sub(request):
	view_logger.info("Received request from subscription.")
	mode         = request.GET.get('hub.mode')
	view_logger.info("Got hub.mode value: " + mode)
	challenge    = request.GET.get('hub.challenge')
	view_logger.info("Got hub.challenge value: " + challenge)
	verify_token = request.GET.get('hub.verify_token')
	view_logger.info("Got hub.verify_token value: " + verify_token)
	if challenge:
		view_logger.info("Sending challenge to Instagram")
	    return HttpResponse(challenge)
	else:
		reactor = subscriptions.SubscriptionsReactor()
		view_logger.info("Creating Subscription Reactor...")
		reactor.register_callback(subscriptions.SubscriptionType.TAG, parse_instagram_update)
		view_logger.info("Registering callback from reactor...")

		x_hub_signature = request.headers.get('X-Hub-Signature')
		view_logger.info("Getting X-Hub-Signature: "+x_hub_signature)
		raw_response    = request.body.read()
		view_logger.info("Getting subscription JSON response"+raw_response)
		try:
			reactor.process(CONFIG['client_secret'], raw_response, x_hub_signature)
			view_logger.info("Processing subscription...")
		except subscriptions.SubscriptionVerifyError:
			view_logger.error('Instagram signature mismatch')
	return Response('Parsed instagram')

def parse_instagram_update(update):
	#TODO: CALL MODEL HERE FOR GETTING CONCERT WITH THE SUBSCRIPTION ID OR TAG
	#AFTER THAT MAKE THE CALL TO INSTAGRAM TO GET THE RECENT MEDIA
	view_logger.info("Processing update." + update)