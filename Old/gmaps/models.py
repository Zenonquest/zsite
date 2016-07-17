import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Coordinates(models.Model):
	name = models.TextField(max_length=200)
	longitude = models.FloatField(max_length=200)
	latitude = models.FloatField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.name

