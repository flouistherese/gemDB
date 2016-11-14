# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gemDatabase', '0041_instrumentfamily_currency_pair'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rounding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=10, max_digits=30, null=True)),
                ('instrument_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gemDatabase.InstrumentType')),
            ],
            options={
                'db_table': 'roundings',
            },
        ),
    ]