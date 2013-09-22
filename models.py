from django.db import models
from django.template.defaultfilters import slugify
from djangotoolbox.fields import ListField, EmbeddedModelField

class Event(models.Model):
	type_of_event = models.CharField(max_length=25)
	date = models.DateField()
	


class Concert(models.Model):
	event_info = models.ForeignKey('Event')
	concert_id = models.AutoField(primary_key=True)
	main_artist = models.ForeignKey('Artist')
	openers = ListField(EmbeddedModelField('Opener'))
	venue = models.ForeignKey('Venue')
	subscription_id = models.CharField(max_length=100)
	instagram_tag = models.CharField(max_length=50)
	media = ListField(EmbeddedModelField('Picture'))
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.main_artist.name

	def save(self, *args, **kwargs):
		if not self.concert_id:
			# Newly created object, so set slug
			self.slug = slugify(self.main_artist.name)
		
		super(Concert, self).save(*args, **kwargs)


class Opener(Concert):
	pass

class Venue(models.Model):
	city = models.CharField(max_length=50)
	venue_name = models.CharField(max_length=50)
	venue_location_lat = models.CharField(max_length=50)
	venue_location_long = models.CharField(max_length=50)
	foursquare_location_id = models.CharField(max_length=100)
	instagram_location_id = models.CharField(max_length=25)
	
class Artist(models.Model):
	name = models.CharField(max_length=50)
	info = models.CharField(max_length=255)

class Picture(models.Model):
	instagram_user = models.CharField(max_length=50)
	standard_url = models.CharField(max_length=255)
	low_res_url = models.CharField(max_length=255)
	thumbnail_url = models.CharField(max_length=255)
	votes = models.CharField(max_length=15)
