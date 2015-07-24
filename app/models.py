from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):
	name = models.CharField(max_length=50)
	slug = AutoSlugField(populate_from='name', unique=True)

	def __str__(self):
		return "{0}".format(self.name)


class Drink(models.Model):
	name = models.CharField(max_length=100)
	price = models.FloatField()
	category = models.ForeignKey('app.Category')

	def __str__(self):
		return "{0} - {1}".format(self.name, self.price)