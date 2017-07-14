# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finpy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='cashflow',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stock',
            name='current_ratio',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stock',
            name='debt_equity_ratio',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stock',
            name='profit_margin',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stock',
            name='return_on_assets',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
