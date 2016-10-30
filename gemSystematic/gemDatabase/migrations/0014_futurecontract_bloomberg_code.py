# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 14:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gemDatabase', '0013_datafeed_bloomberg_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='futurecontract',
            name='bloomberg_code',
            field=models.CharField(default='CME/CLJ2017', max_length=20),
            preserve_default=False,
        ),
    ]
