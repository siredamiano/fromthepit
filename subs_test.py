from instagram.client import InstagramAPI
from instagram import subscriptions
import sys
import os

sys.path.append('')
os.environ['DJANGO_SETTINGS_MODULE'] = 'fromthepit.settings'

CONFIG = {
    'client_id': '',
    'client_secret': '',
	'callback_url': ''
}

def do_tag_subscription(client, tag):
	client.create_subscription(object='tag',object_id=tag, aspect='media', callback_url=CONFIG['callback_url'])
	print 'Made the subscription to tag: ' + tag
	
def do_location_subscription(client, location_id):
	client.create_subscription(object='location',object_id=location_id, aspect='media', callback_url=CONFIG['callback_url'])
	print 'Made the subscription to location: ' + location_id

def delete_subscription(client, id):
	client.delete_subscriptions(id=id)
	print instagram_client.list_subscriptions()



instagram_client = InstagramAPI(client_id=CONFIG['client_id'], client_secret=CONFIG['client_secret'])

print 'Open connection to Instagram API'
tag = 'muse'
#location = 185096
do_tag_subscription(instagram_client,tag)
#do_location_subscription(instagram_client, location)

subs_list = instagram_client.list_subscriptions()

print subs_list

#index = 0
#for data in subs_list['data']:
#	if data['object_id'] == tag:
#		print data['id']

#delete_subscription(instagram_client,3074992)



