# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finpy', '0002_auto_20170706_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='PBook_ratio',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='PE_ratio',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
