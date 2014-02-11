import os
import sys

sys.path.append('/home/siredamiano/webapps/fromthepit')
os.environ['DJANGO_SETTINGS_MODULE'] = 'fromthepit.settings'

view_logger = logging.getLogger('logview.view_logs')
hdlr = logging.FileHandler('/home/siredamiano/webapps/fromthepit/logs/views.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(funcName)s %(filename)s %(lineno)d %(message)s')
hdlr.setFormatter(formatter)
view_logger.addHandler(hdlr) 
view_logger.setLevel(logging.DEBUG)

def delete_bad_links(concert_object):
	import urllib2
	list_before_len = len(concert_object.media)
	view_logger.info("Getting list current length: " + str(list_before_len))
	
	view_logger.info("Starting to check for bad links.")
	for picture in concert_object.media:
		try:
			page = urllib2.urlopen(picture)
			if page.getcode() == 200:
				pass
		except urllib2.HTTPError:
			concert_object.media.remove(picture)
			view_logger.info("Removing link from list: " + picture)
	
	view_logger.info("Evaluating if links were removed.")
	if len(concert_object.media) < list_before_len:
		concert_object.save()
		view_logger.info("Saving concert object.")
	else:
		view_logger.info("All links are good to go!")