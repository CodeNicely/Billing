from __future__ import unicode_literals

from django.db import models
from item.models import item_data

# Create your models here.


class order_data_purchase(models.Model):
	order_id = models.CharField(max_length=120,primary_key=True)
	item_name = models.CharField(max_length=120,null=True,blank=True)
	customer_id=models.CharField(max_length=120,null=True,blank=True)
	customer_name=models.CharField(max_length=120,null=True,blank=True)
	tax_id=models.CharField(max_length=120,null=True,blank=True)
	sub_total=models.FloatField(max_length=120)
	tax_total=models.FloatField(max_length=120,null=True)
	grand_total=models.FloatField(max_length=120,null=True)
	date_created=models.DateField(auto_now_add=True)
	date_modified=models.DateField(auto_now_add=True)
	payment_status=models.BooleanField(default=False)
	payment_mode=models.CharField(max_length=120,null=True,blank=True)
	payment_description=models.TextField(max_length=250,null=True)


class order_data_selling(models.Model):
	order_id = models.IntegerField(null=True,blank=True)
	customer_id=models.CharField(max_length=120,null=True,blank=True)
	customer_name=models.CharField(max_length=120,null=True,blank=True)
	order_type=models.CharField(max_length=120,null=True,blank=True,choices=[('Purchase', 'Purchase'), ('Sell', 'Sell')])
	tax_id=models.CharField(max_length=120,null=True,blank=True)
	sub_total=models.FloatField(max_length=120,null=True)
	tax_total=models.FloatField(max_length=120,null=True)
	grand_total=models.FloatField(max_length=120,null=True)
	date_created=models.DateField(auto_now_add=True)
	date_modified=models.DateField(auto_now_add=True)
	payment_status=models.BooleanField(default=False)
	payment_mode=models.CharField(max_length=120,null=True,blank=True)
	payment_description=models.TextField(max_length=250,null=True)


class order_item(models.Model):
      order_id=models.IntegerField()
      item_id=models.ForeignKey(item_data,to_field='item_id')
      created=models.DateField(auto_now_add=True)
      modified=models.DateField(auto_now_add=True)
      price=models.FloatField(null=True)
      quantity=models.IntegerField(null=True)
      total_tax=models.FloatField(null=True)
      tax=models.FloatField(null=True)

