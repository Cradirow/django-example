from django.db import models

class Movie(models.Model):
	title = models.CharField(max_length=30)
	genre = models.CharField(max_length=15)
	year = models.IntegerField()

	def __str__(self):
		return self.title

class Caster(models.Model):
	name = models.CharField(max_length=15)
	date = models.CharField(max_length=15)	
	did = models.CharField(max_length=100)
	do = models.CharField(max_length=100)

	def __str__(self):
		return self.name
