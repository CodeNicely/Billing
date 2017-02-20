from __future__ import unicode_literals

from django.db import models

class Tax_Table(models.Model):
	name=models.CharField(max_length=15)
	value=models.FloatField()
	created=models.DateField()
	modified=models.DateField()
