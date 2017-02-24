from __future__ import unicode_literals

from django.db import models

class expense_data(models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField(max_length=200)
	amount=models.FloatField()
	created=models.DateTimeField(auto_now_add=False)
	modified=models.DateTimeField(auto_now_add=False)