# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expense', '0004_auto_20170224_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense_data',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='expense_data',
            name='modified',
            field=models.DateField(),
        ),
    ]