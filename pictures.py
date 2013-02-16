from instagram.client import InstagramAPI

import logging


class InstagramApiWrapper:
    
    
    def __init__(self,client_id, s_client_id, callback_url):
        self._client_id = client_id
        self._s_client_id = s_client_id
		self.callback_url = callback_url
        self.standard_resolution_pictures = []
        self.low_resolution_pictures = []


    def searchPicturesByTag(self,count, tag):
        api = InstagramAPI(client_id=self._client_id,      client_secret=self._s_client_id)
        search_media, next = api.tag_recent_media(count=count,tag_name=tag)
        for media in search_media:
            self.standard_resolution_pictures.append(media.images['standard_resolution'].url)
            self.low_resolution_pictures.append(media.images['low_resolution'].url)

    def searchPicturesbyLocation(self,count, max_id, location_id):
		api = InstagramAPI(client_id=self._client_id,      client_secret=self._s_client_id)
		recent_media , next = api.location_recent_media(count=count, max_id, location_id)
		pass
		
		
	def create_subscription_by_tag(self, tag ):
		api = InstagramAPI(client_id=self._client_id,      client_secret=self._s_client_id)
		api.create_subscription(object='tag',object_id=tag, aspect='media', callback_url=self.callback_url)
		