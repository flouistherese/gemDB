# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gemDatabase', '0015_addCurrencyPairs'),
    ]

    operations = [
        migrations.AddField(
            model_name='currencypair',
            name='bloomberg_code',
            field=models.CharField(default='GBPUSD', max_length=20),
            preserve_default=False,
        ),
    ]
