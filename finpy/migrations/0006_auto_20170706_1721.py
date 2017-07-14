# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finpy', '0005_auto_20170706_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='PEG_ratio',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='beta',
            field=models.FloatField(default=5, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='cashflow',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='current_ratio',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='debt_equity_ratio',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='profit_margin',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='return_on_assets',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='revenueGrowth',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
