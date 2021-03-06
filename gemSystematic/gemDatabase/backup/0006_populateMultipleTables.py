# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 13:49
from __future__ import unicode_literals

from django.db import models, migrations
from gemDatabase.models import *


def populate_multiple_tables(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    DataPointType(code = "OPEN", description = "Open").save()
    DataPointType(code = "LOW", description = "Low").save()
    DataPointType(code = "HIGH", description = "High").save()
    DataPointType(code = "CLOSE", description = "Close").save()
    DataPointType(code = "VOLUME", description = "Volume").save()
    DataPointType(code = "OPEN_INTEREST", description = "Open Interest").save()

    DataPointSource(code = "BBG", description = "Bloomberg").save()

    Exchange(code = "CME", description = "Chicago Mercantile Exchange").save()
    Exchange(code = "CBOT", description = "Chicago Board of Trade").save()
    Exchange(code = "ICE", description = "Intercontinental Exchange").save()
    Exchange(code = "LME", description = "London Metal Exchange").save()
    Exchange(code = "EUREX", description = "Eurex").save()
    Exchange(code = "COMEX", description = "Comex").save()

    SettlementType(code = "CASH", description = "Cash Settlement").save()
    SettlementType(code = "PHYSICAL", description = "Physical Settlement").save()

class Migration(migrations.Migration):

    dependencies = [
        ('gemDatabase', '0005_auto_20161022_1347'),
    ]

    operations = [
    	migrations.RunPython(populate_multiple_tables),
    ]
