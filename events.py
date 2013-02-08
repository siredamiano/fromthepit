
class Event:
	
	def __init__(self, date):
		self.date = date
		
	def get_date():
		return self.date
	
	def set_date(self,date):
		self.date = date	
	
class Concert(Event):
	
	def __init__(self, artist, openers,venue):
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

class Venue():
	
	def __init__(self, venue_name, country,city, state, info, location):
		self.venue_name = venue_name
		self.country = country
		self.city = city
		self.state = state
		self.info = info
		self.location = location