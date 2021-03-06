# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 14:51
from django.db import models, migrations
from gemDatabase.models import *

def populate_strategies(apps, schema_editor):
	StrategyType(code = 'MOMENTUM', description = 'Momentum').save()
	StrategyType(code = 'VALUE', description = 'Value').save()
	StrategyType(code = 'CARRY', description = 'Carry').save()

	Strategy(code = 'ENERGY_MOM', description = 'Energy Momentum', strategy_type_id = StrategyType['MOMENTUM'].id).save()
	Strategy(code = 'FX_MOM', description = 'FX Momentum', strategy_type_id = StrategyType['MOMENTUM'].id).save()
	Strategy(code = 'BOND_MOM', description = 'Bond Momentum', strategy_type_id = StrategyType['MOMENTUM'].id).save()
	Strategy(code = 'INDEX_MOM', description = 'Index Momentum', strategy_type_id = StrategyType['MOMENTUM'].id).save()
	Strategy(code = 'BOND_VALUE', description = 'Bond Value', strategy_type_id = StrategyType['VALUE'].id).save()
	Strategy(code = 'FX_CARRY', description = 'FX Carry', strategy_type_id = StrategyType['CARRY'].id).save()


	TradingModel(code = 'ENERGY_MOM_CL', description = 'Energy Momentum CL', strategy_id = Strategy['ENERGY_MOM'].id).save()
	TradingModel(code = 'ENERGY_MOM_NG', description = 'Energy Momentum NG', strategy_id = Strategy['ENERGY_MOM'].id).save()
	TradingModel(code = 'BOND_MOM_TY', description = 'Bond Momentum TY', strategy_id = Strategy['BOND_MOM'].id).save()
	TradingModel(code = 'FX_MOM_GBP', description = 'FX Momentum GBPUSD', strategy_id = Strategy['FX_MOM'].id).save()
	TradingModel(code = 'BOND_VALUE_FV', description = 'Bond Value FV', strategy_id = Strategy['BOND_VALUE'].id).save()
	TradingModel(code = 'FX_CARRY_AUDJPY', description = 'FX MomentCarry AUDJPY', strategy_id = Strategy['FX_CARRY'].id).save()

	TradingModelFeed(trading_model_id = TradingModel['ENERGY_MOM_CL'].id, data_feed_id = DataFeed["CL1"].id).save()
	TradingModelFeed(trading_model_id = TradingModel['BOND_MOM_TY'].id, data_feed_id = DataFeed["TY1"].id).save()
	TradingModelFeed(trading_model_id = TradingModel['ENERGY_MOM_NG'].id, data_feed_id = DataFeed["NG1"].id).save()
	TradingModelFeed(trading_model_id = TradingModel['FX_MOM_GBP'].id, data_feed_id = DataFeed["GBPUSD_SPOT"].id).save()
    
class Migration(migrations.Migration):

    dependencies = [
        ('gemDatabase', '0021_addFutureMonths'),
    ]

    operations = [
    	migrations.RunPython(populate_strategies),
    ]
