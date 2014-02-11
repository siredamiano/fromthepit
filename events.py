
from fromthepit.models import Concert
from fromthepit.pictures import InstagramApiWrapper
from instagram.client import InstagramAPI
from instagram.bind import InstagramAPIError

CONFIG = {
    'client_id': '',
    'client_secret': '',
	'callback_url': ''
}



class Event:
	
	def __init__(self, date, instagram_tag):
		self.date = date
		self.instagram_tag = instagram_tag
		
	def get_date():
		return self.date
	
	def set_date(self,date):
		self.date = date
	
	def get_instagram_tag():
		return self.instagram_tag
		
	def set_instagram_tag(self, instagram_tag):
		self.instagram_tag = instagram_tag
		
	def create_subscription(tag):
		ig_api = InstagramApiWrapper(CONFIG['client_id'], CONFIG['client_secret'], CONFIG['callback_url'])
		ig_api.create_subscription_by_tag(tag)
		subs_list = ig_api.list_subscription()
		pass
	
class Concert(Event):
	
	def __init__(self, date, instagram_tag, artist, openers,venue):
		super.__init__(date, instagram_tag)
		self.artist = artist
		self.openers = openers
		self.venue = venue
		
	def get_artist():
		return self.artist
	
	def get_openers():
		return self.openers
	
	def get_venue():
		return self.venue
		
	def set_artist(self,artist):
		self.artist = artist
	
	def set_openers(self,openers):
		self.openers = openers	
		
	def set_venue(self, venue):
		self.venue = venue
		
	def create_concert(self):
		try:
			ig_api = InstagramApiWrapper(CONFIG['client_id'], CONFIG['client_secret'], CONFIG['callback_url'])
			concert = Concert(main_artist=self.artist,openers=self.openers,concert_date=super.getDate(),venue_name=self.venue.get_venue_name(), media=ig_api.standard_resolution_pictures, instagram_tag=super.get_instagram_tag())
			super.create_subscription(super.get_instagram_tag())
		except InstagramAPIError:
			return InstagramAPIError.__str__
			
		#TODO: HERE WE ARE GOING TO CREATE THE CONCERT OBJECT TO DB AND SAVE IT. ALSO CALL THE SUBSCRIPTION
		pass

class Venue():
	
	def __init__(self, venue_name, country,city, state, venue_info, location):
		self.venue_name = venue_name
		self.country = country
		self.city = city
		self.state = state
		self.venue_info = venue_info
		self.location = location
			
	def get_venue_name():
		return self.venue_name

	def get_country():
		return self.country

	def get_city():
		return self.city	
		
	def get_state():
		return self.state

	def get_venue_info():
		return self.venue_info

	def get_location():
		return self.location		
		
		
		
		
		
		
		
		
		
		
		
		
		
