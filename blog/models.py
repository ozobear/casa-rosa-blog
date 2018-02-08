from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	title = models.CharField(max_length=125)
	slug = models.SlugField(unique=True, max_length=255)
	author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
	description = models.CharField(max_length=250)
	content = models.TextField()
	image = models.ImageField(blank=True)
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	class Meta:
		ordering = ['-publish']

	def __str__(self):
		return self.title

	def published(self):
            self.created = timezone.now()
            self.save()
