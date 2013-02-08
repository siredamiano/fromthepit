from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField

class Event(models.Model):
    kind = models.ForeignKey('Concert')
		

class Concert(models.Model):
    main_artist = models.CharField(max_length=255)
	concert_id = models.IntegerField()
    openers = ListField(EmbeddedModelField('Opener'))
    concert_date = models.DateField()
    venue_location = models.CharField(max_length = 255)
	venue_location_coordinates = models.CharField(max_length = 255)
    media = ListField()
    slug = models.SlugField(unique=True)
    subscription_id = models.CharField(max_length=255)
	instagram_tag = models.CharField(max_length=255)
	
    def __unicode__(self):
        return self.main_artist


class Opener(models.Model):
    artist_name = models.CharField(max_length=255)
    opener_media = ListField()
    
