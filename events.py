
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
		
	def create_concert():
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
		
		
		
		
		
		
		
		
		
		
		
		
		