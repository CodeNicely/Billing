# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expense', '0003_auto_20170222_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense_data',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='expense_data',
            name='modified',
            field=models.DateTimeField(),
        ),
    ]
