# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_data_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_data',
            name='order_id',
            field=models.IntegerField(blank=True, default=True, null=True),
        ),
    ]
