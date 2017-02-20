# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(max_length=20)),
                ('order_type', models.CharField(max_length=120)),
                ('sub_total', models.FloatField(max_length=120)),
                ('tax_total', models.FloatField(max_length=120)),
                ('grand_total', models.FloatField(max_length=120)),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
                ('payment_mode', models.CharField(max_length=120)),
                ('payment_status', models.CharField(max_length=120)),
                ('payment_description', models.TextField(max_length=250)),
            ],
        ),
    ]
