import pylast

API_KEY = "648cd04627171fd89c2881c6a27c5bb1" 
API_SECRET = "is b6357b416bdcdee587ff37fc28f70895"

username = ""
password_hash = pylast.md5("")

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
    API_SECRET, username = username, password_hash = password_hash)

venues = network.search_for_venue("Terminal 5", "United States")

for venue in venues.get_next_page():
	events = venue.get_upcoming_events()
        for event in events:
		    print "Title of Event: " + event.get_title()
		    print "Headliner: " + event.get_headliner().get_name(True)
		    
		    artists = event.get_artists()
		    print "Openers: "
		    for artist in artists:
			    print artist.get_name(True)
		 
		    print "Start Date: " + event.get_start_date() + "\n"