# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 00:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gemDatabase', '0004_futurecontract_first_notice_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField()),
            ],
            options={
                'db_table': 'reports',
            },
        ),
        migrations.CreateModel(
            name='ReportItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ignored', models.BooleanField(default=False)),
                ('z_score', models.DecimalField(decimal_places=4, max_digits=8, null=True)),
                ('data_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gemDatabase.DataPoint')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gemDatabase.Report')),
            ],
            options={
                'db_table': 'report_items',
            },
        ),
        migrations.CreateModel(
            name='ReportType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'report_types',
            },
        ),
        migrations.AddField(
            model_name='report',
            name='report_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gemDatabase.ReportType'),
        ),
    ]
