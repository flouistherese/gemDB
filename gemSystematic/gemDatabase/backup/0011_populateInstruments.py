# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 18:32
from __future__ import unicode_literals

from django.db import models, migrations
from gemDatabase.models import *

def populate_instruments(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.

    Instrument(code = "BLK", description = "BlackRock Inc. stock", instrument_type = InstrumentType["STOCK"]).save()
    Instrument(code = "AAPL", description = "Apple Inc. stock", instrument_type = InstrumentType["STOCK"]).save()
    Instrument(code = "TSLA", description = "Tesla Inc. stock", instrument_type = InstrumentType["STOCK"]).save()

    Stock(code = "BLK", description = "BlackRock Inc. stock", bloomberg_code = "WIKI/BLK", company = "BlackRock Inc.", currency = Currency["USD"], instrument = Instrument["BLK"]).save()
    Stock(code = "AAPL", description = "Apple Inc. stock", bloomberg_code = "WIKI/AAPL", company = "Apple Inc.", currency = Currency["USD"], instrument = Instrument["AAPL"]).save()
    Stock(code = "TSLA", description = "Tesla Inc. stock", bloomberg_code = "WIKI/TSLA", company = "Tesla Inc.", currency = Currency["USD"], instrument = Instrument["TSLA"]).save()

    InstrumentFamily(code = "BLK", description = "BlackRock Inc. stock instrument family", stock = Stock["BLK"]).save()
    InstrumentFamily(code = "AAPL", description = "Apple Inc. stock instrument family", stock = Stock["AAPL"]).save()
    InstrumentFamily(code = "TSLA", description = "Tesla Inc. stock instrument family", stock = Stock["TSLA"]).save()
    
    

class Migration(migrations.Migration):

    dependencies = [
        ('gemDatabase', '0005_populateCurrencies'),
    ]

    operations = [
    	migrations.RunPython(populate_instruments),
    ]
