from __future__ import unicode_literals

from django.db import models

class city_table(models.Model):
	city_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=15)

