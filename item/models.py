from __future__ import unicode_literals

from django.db import models

# Create your models here.
class item_data(models.Model):
	item_id=models.IntegerField()
	item_name=models.CharField(max_length=120)
	description=models.TextField()
	price=models.FloatField()
	unit=models.CharField(max_length=120)
	created=models.DateField(auto_now_add=True)
	modified=models.DateField(auto_now_add=True)