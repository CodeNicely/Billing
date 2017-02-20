from __future__ import unicode_literals

from django.db import models

# Create your models here.


class order_data(models.Model):
	customer_name=models.CharField(max_length=120,null=True,blank=True)
	order_type=models.CharField(max_length=120,null=True,blank=True,choices=[('Purchase', 'Purchase'), ('Sell', 'Sell')])
	tax=models.CharField(max_length=120,null=True,blank=True)
	sub_total=models.FloatField(max_length=120)
	tax_total=models.FloatField(max_length=120)
	grand_total=models.FloatField(max_length=120)
	date_created=models.DateTimeField(auto_now=False, auto_now_add=False)
	date_modified=models.DateTimeField(auto_now=False, auto_now_add=False)
	payment_status=models.BooleanField()
	payment_mode=models.CharField(max_length=120,null=True,blank=True)
	payment_description=models.TextField(max_length=250)



