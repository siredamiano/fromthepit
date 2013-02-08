from django.shortcuts import render_to_response
from django.template import RequestContext
from fromthepit.pictures import InstagramApiWrapper
from fromthepit.models import Concert
from datetime import *
from django.http import HttpResponse
import logging


CONFIG = {
    'client_id': 'ff1a989e5b4949a38fcd3d32f51a59d9',
    'client_secret': '3e73e09b36074d68a04023fa5cfdae4f'
}

view_logger = logging.getLogger('logview.view_logs')

def showPictures(request):
	apiCall = InstagramApiWrapper(CONFIG['client_id'],CONFIG['client_secret'])
	view_logger.info("Configured Instagram API.")
	
	apiCall.searchPicturesByTag(50,'palmaviolets')
	view_logger.info("Made call to Instagram with the tag info.")
	concert = Concert(main_artist='Palma Violets',openers=[],concert_date=date.today(),location='Pianos', media=apiCall.standard_resolution_pictures,slug='palma-violets')
	view_logger.info("Created concert object to save in database.")
	concert.save()
	view_logger.info("Save concert object to db.")
	concerts = Concert.objects.filter(slug='palma-violets')
	view_logger.info("Look into db for list of media.")
	context = {'concerts': concerts}
	view_logger.info("Created context to send in the response.")
	return render_to_response('testpictures.html', context, context_instance=RequestContext(request))


def hello(request):
	return HttpResponse("Hello from django")