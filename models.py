from django.db import models
rom django.template.defaultfilters import slugify
from djangotoolbox.fields import ListField, EmbeddedModelField

class Event(models.Model):
	kind = models.ForeignKey('Concert')
		

class Concert(models.Model):
	main_artist = models.CharField(max_length=255)
	openers = ListField(EmbeddedModelField('Opener'))
	concert_date = models.DateField()
	venue_name = models.CharField(max_length = 255)
	venue_location_coordinates = models.CharField(max_length = 255)
	media = ListField()
	slug = models.SlugField(unique=True)
	concert_id = models.IntegerField(primary_key=True)
	subscription_id = models.CharField(max_length=255)
	instagram_tag = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.main_artist

	def save(self, *args, **kwargs):
		if not self.id:
			# Newly created object, so set slug
			self.slug = slugify(self.main_artist)

			super(Concert, self).save(*args, **kwargs)


class Opener(models.Model):
	artist_name = models.CharField(max_length=255)
	opener_media = ListField()
	

class Venue(models.Model):
	pass
    
