from __future__ import unicode_literals

from django.db import models

class Tax(models.Model):
	name=models.CharField(max_length=15)
	tax_id=models.IntegerField()
	item_id=models.IntegerField(null=True)
	created=models.DateField()
	modified=models.DateField()