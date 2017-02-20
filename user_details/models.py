from __future__ import unicode_literals

from django.db import models

# Create your models here.

class user_data(models.Model):
	user_name=models.CharField(max_length=120,null=True,blank=True)
	mobile=models.IntegerField()
	email=models.EmailField()
	firm_name= models.CharField(max_length=120,null=True,blank=True)
	address=models.CharField(max_length=120,null=True,blank=True)
	city=models.CharField(max_length=120,null=True,blank=True,choices=[('Raipur', 'Raipur'), ('Bhilai', 'Bhilai')])
	user_type=models.CharField(max_length=120,null=True,blank=True)