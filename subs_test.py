from instagram.client import InstagramAPI
from instagram import subscriptions

CONFIG = {
    'client_id': 'ff1a989e5b4949a38fcd3d32f51a59d9',
    'client_secret': '3e73e09b36074d68a04023fa5cfdae4f',
	'callback_url': 'http://fromthepit.us/sub'
}


instagram_client = InstagramAPI(client_id=CONFIG['client_id'], client_secret=CONFIG['client_secret'])
print 'Open connection to Instagram API'
tag = 'gojira'
instagram_client.create_subscription(object='tag',object_id=tag, aspect='media', callback_url=CONFIG['callback_url'])
print 'Made the subscription to tag: ' + tag

tag = 'theatlasmoth'
instagram_client.create_subscription(object='tag',object_id=tag, aspect='media', callback_url=CONFIG['callback_url'])
print 'Made the subscription to tag: ' + tag

subs_list = instagram_client.list_subscriptions()

print subs_list

index = 0
tag = 'gojira'
for data in subs_list['data']:
	if data['object_id'] == tag:
		print data['id']

instagram_client.delete_subscriptions(id=2896995)
instagram_client.delete_subscriptions(id=2896996)

print instagram_client.list_subscriptions()

