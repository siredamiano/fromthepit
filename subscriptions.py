from instagram.client import InstagramAPI
from instagram import subscriptions


CONFIG = {
    'client_id': 'ff1a989e5b4949a38fcd3d32f51a59d9',
    'client_secret': '3e73e09b36074d68a04023fa5cfdae4f',
	'callback_url': 'http://4i24.localtunnel.com/sub'
}
	

class Subscription:	
	
	def __init__(self):
		self.instagram_client = InstagramAPI(client_id=CONFIG['client_id'], client_secret=CONFIG['client_secret'])
	
	@staticmethod
	def subscribeByTag(self,tag):	
		self.instagram_client.create_subscription(object='tag',object_id=tag, aspect='media', callback_url=CONFIG['callback_url'])
		
	def subscribeByLoc(self,loc):
		self.instagram_client.create_subscription(object='location', object_id=loc, aspect='media', callback_url=CONFIG['callback_url'])
	
	@staticmethod
	def listSubscriptions(self):
		print self.instagram_client.list_subscriptions()
		
	def deleteSubscription(self,id):
		self.instagram_client.delete_subscriptions(id=id)


subs = Subscription()
print 'Making subscription to Instagram'
subs.subscribeByTag(subs,'localnatives')
#subs.listSubscriptions(subs)
print'Sending subscription with tag'



