
class Event:
	
	def __init__(self, date):
		pass
	
	
class Concert(Event):
	
	def __init__(self, artist, openers, date, venue):
		self.artist = artist
		self.openers = openers
		self.date = date
		self.venue = venue
		
	def get_artist():
		return self.artist
	
	def get_openers():
		return self.openers
		
	def get_date():
		return self.date
	
	def get_venue():
		return self.venue
		
	def set_artist(self,artist):
		self.artist = artist
	
	def set_openers(self,openers):
		self.openers = openers	
	
	def set_artist(self,date):
		self.date = date
		
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