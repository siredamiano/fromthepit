from instagram.client import InstagramAPI
from instagram import subscriptions

CONFIG = {
    'client_id': 'ff1a989e5b4949a38fcd3d32f51a59d9',
    'client_secret': '3e73e09b36074d68a04023fa5cfdae4f',
	'callback_url': 'http://4c53.localtunnel.com/sub'
}


instagram_client = InstagramAPI(client_id=CONFIG['client_id'], client_secret=CONFIG['client_secret'])
print 'Open connection to Instagram API'
tag = 'tysegall'
instagram_client.create_subscription(object='tag',object_id=tag, aspect='media', callback_url=CONFIG['callback_url'])
print 'Made the subscription to tag' + tag