from __future__ import unicode_literals

from django.db import models

class unit_table(models.Model):
	unit_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=15)
