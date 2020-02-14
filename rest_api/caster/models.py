from django.db import models

class Caster(models.Model):
	name = models.CharField(max_length=15)
	time = models.CharField(max_length=20)
	did = models.CharField(max_length=1000)
	todo = models.CharField(max_length=1000)
	ref = models.CharField(max_length=1000)

	def __str__(self):
		return 'Name: ', self.name, '\n', 'Time: ', self.time
