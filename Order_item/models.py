from __future__ import unicode_literals

from django.db import models

class Order_item(models.Model):
      order_id=models.IntegerField()
      item_id=models.IntegerField(blank=True,null=True)
      created=models.IntegerField()
      modified=models.IntegerField()
      price=models.FloatField()
      quantity=models.IntegerField()
      total_tax=models.FloatField()
      tax=models.FloatField()
