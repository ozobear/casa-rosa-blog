from django.db import models
from embed_video.fields import EmbedVideoField

class Artist(models.Model):
	name = models.CharField(max_length=100)
	video = EmbedVideoField(blank=True)
	image = models.ImageField(blank=False)
	slug = models.SlugField(unique=True, max_length=60)
	description = models.TextField()

	class Meta:
		ordering = ['-name']

	def __str__(self):
		return self.name
