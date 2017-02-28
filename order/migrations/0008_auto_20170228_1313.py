# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20170228_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_data_purchase',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order_data_purchase',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order_data_selling',
            name='payment_status',
            field=models.BooleanField(default=False),
        ),
    ]