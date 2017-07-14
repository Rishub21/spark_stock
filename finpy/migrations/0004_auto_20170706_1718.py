# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finpy', '0003_auto_20170706_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='EPS_ratio',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='last_price',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
