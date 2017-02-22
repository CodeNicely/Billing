from __future__ import unicode_literals


from django.db import models

class Item(models.Model):
	item_id=models.AutoField(primary_key=True,default=True)
	name=models.CharField(max_length=15)
	description=models.CharField(max_length=25)
	price=models.FloatField()
	unit=models.IntegerField(null=True)
	created=models.DateField()
	modified=models.DateField()

