# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gemDatabase', '0003_auto_20161027_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='futurecontract',
            name='first_notice_date',
            field=models.DateField(default='2016-05-01'),
            preserve_default=False,
        ),
    ]
