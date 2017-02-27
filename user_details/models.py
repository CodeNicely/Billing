from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user_data(models.Model):
	user_id=models.IntegerField()
	user_name=models.CharField(max_length=120)
	mobile=models.IntegerField()
	email=models.EmailField()
	firm_name=models.CharField(max_length=120)
	address=models.CharField(max_length=120)
	created=models.DateField(auto_now_add=True)
	modified=models.DateField(auto_now_add=True)