from __future__ import unicode_literals

from django.db import models

class expense_data(models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField(max_length=200)
	amount=models.FloatField()
	created=models.DateField(auto_now_add=True)
	modified=models.DateField(auto_now_add=True)