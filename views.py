from django.shortcuts import render_to_response
from django.template import RequestContext
from fromthepit.pictures import InstagramApiWrapper
from fromthepit.models import Concert
from datetime import *
from django.http import HttpResponse
import logging


CONFIG = {
'client_id': 'ff1a989e5b4949a38fcd3d32f51a59d9',
'client_secret': '3e73e09b36074d68a04023fa5cfdae4f',
'callback_url':'demo.fromthepit.us/sub'
}

view_logger = logging.getLogger('logview.view_logs')

def showPictures(request):
	concerts = Concert.objects.get(slug='dan-deacon')
	view_logger.info("Look into db for list of media.")
	context = {'concerts': concerts}
	view_logger.info("Created context to send in the response.")
	return render_to_response('testpictures.html', context, context_instance=RequestContext(request))

def showPicturesCoachella(request):
	concerts = Concert.objects.get(slug='coachella')
	view_logger.info("Look into db for list of media.")
	view_logger.info("Deleting bad links from concert list for: " + concerts.main_artist.name)
	delete_bad_links(concerts)
	context = {'concerts': concerts}
	view_logger.info("Created context to send in the response.")
	return render_to_response('testpictures.html', context, context_instance=RequestContext(request))


def hello(request):
	return HttpResponse("Hello from django")
		
	
	

def delete_bad_links(concert_object):
	import urllib2
	list_before_len = len(concert_object.media)
	view_logger.info("Getting list current length: " + str(list_before_len))
	
	view_logger.info("Starting to check for bad links.")
	
	for picture in concert_object.media:
		try:
			page = urllib2.urlopen(picture.standard_url)
			if page.getcode() == 200:
				return
		except urllib2.HTTPError:
			concert_object.media.remove(picture)
			view_logger.info("Removing link from list: " + picture.standard_url)
			
	view_logger.info("Evaluating if links were removed.")
	if len(concert_object.media) < list_before_len:
		concert_object.save()
		view_logger.info("Saving concert object.")
	else:
		view_logger.info("All links are good to go!")
		
	
