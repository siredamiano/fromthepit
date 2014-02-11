from celery import task
from django.core.exceptions import *
from fromthepit.models import *
from fromthepit.pictures import InstagramApiWrapper
import logging
from datetime import *

CONFIG = {
    'client_id': '',
    'client_secret': '',
	'callback_url': ''
}

task_logger = logging.getLogger('logview.tasks_logs')
hdlr = logging.FileHandler('')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)d %(message)s')
hdlr.setFormatter(formatter)
task_logger.addHandler(hdlr) 
task_logger.setLevel(logging.DEBUG)


@task(name='tasks.fetch_instagram_for_tag')
def fetch_instagram_for_tag(concert_tag):
	
	from fromthepit.pictures import InstagramApiWrapper
	
	ig_api = InstagramApiWrapper(CONFIG['client_id'], CONFIG['client_secret'], CONFIG['callback_url'] )
	task_logger.info('Configuring Instragram API Wrapper...')
	
	ig_api.searchPicturesByTag(1,concert_tag)
	task_logger.info('Getting pictures in Instagram with tag: ' + concert_tag)
	
	concert = Concert.objects.get(instagram_tag=concert_tag)
	task_logger.info('Retrieving concert object from DB for: ' + concert.main_artist.name)

	instagram_user = ig_api.instagram_user
	task_logger.info('Instagram User: ' + instagram_user)
	standard_res_pic = ig_api.standard_resolution_pictures.pop()
	task_logger.info('Standard Resolution URL: ' + standard_res_pic)
	low_res_pic = ig_api.low_resolution_pictures.pop()
	task_logger.info('Low Resolution URL: ' + low_res_pic)
	thumbnail_pic = ig_api.thumbnail_pictures.pop()
	task_logger.info('Thumbnail URL: ' + thumbnail_pic)
	
	try:
		task_logger.info('Getting picture object from db...')
		picture = Picture.objects.get(standard_url__exact=standard_res_pic, 
									low_res_url__exact=low_res_pic,
									thumbnail_url__exact=thumbnail_pic,
									instagram_user__exact=instagram_user)
		task_logger.info('Pictures is in db...')
	
	except Picture.DoesNotExist:
		picture = Picture.objects.create(instagram_user=instagram_user, 
										standard_url=standard_res_pic, 
										low_res_url=low_res_pic,
										thumbnail_url=thumbnail_pic)
		task_logger.info('Creating picture object to be saved in db...')
		concert.media.append(picture)
		task_logger.info('Appending picture object to list...')
		concert.save()
		task_logger.info('Saving concert object to DB...')
										
											
@task(name='tasks.fetch_instagram_for_location')
def fetch_instagram_for_location(location_id):

	from fromthepit.pictures import InstagramApiWrapper

	ig_api = InstagramApiWrapper(CONFIG['client_id'], CONFIG['client_secret'], CONFIG['callback_url'] )
	task_logger.info('Configuring Instragram API Wrapper...')

	ig_api.searchPicturesByLocation(1,location_id)
	task_logger.info('Getting pictures in Instagram with location: ' + location_id)

	concert = Concert.objects.get(event_info__date=date.today(), venue__foursquare_location_id=location_id)
	task_logger.info('Retrieving concert object from DB...')
	
	

	task_logger.info('List of concert pictures inside concert object')
	task_logger.info(concert.media)

	recent_picture = ig_api.standard_resolution_pictures
	instagram_user = ig_api.instagram_user
	task_logger.info('Recent pictures from Instagram API...')
	task_logger.info(recent_picture)

	recent_pic = recent_picture.pop()

	picture = Picture.objects.create(instagram_user=instagram_user, standard_url=recent_pic)


