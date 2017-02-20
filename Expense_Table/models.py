from __future__ import unicode_literals

from django.db import models

class Expense_Table(models.Model):
	title=models.CharField(max_length=15)
	Description=models.CharField(max_length=15)
	amount=models.FloatField()
	created=models.DateField()
	modified=models.DateField()