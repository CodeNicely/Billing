# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20170228_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_data_purchase',
            name='item_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='order_data_selling',
            name='item_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
