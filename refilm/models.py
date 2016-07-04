from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib import admin

class Movie(models.Model):
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )
	title = models.CharField(max_length=200)
	rated = models.CharField(max_length=200)
	released = models.CharField(max_length=50)
	runtime = models.CharField(max_length=200)
	genre = models.CharField(max_length=200)
	director = models.CharField(max_length=200)
	writer = models.CharField(max_length=200)
	actors = models.TextField()
	plot = models.TextField()
	language = models.CharField(max_length=100)
	awards = models.CharField(max_length=50)
	poster = models.URLField(blank=True, null=True)
	metascore = models.CharField(max_length=50)
	imdbrating = models.CharField(max_length=50)
	imdbID = models.CharField(max_length=50, null=True)

	def __str__(self):
		return self.title