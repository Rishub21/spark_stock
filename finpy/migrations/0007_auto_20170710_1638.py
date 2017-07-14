# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('finpy', '0006_auto_20170706_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='last_price',
            new_name='current_price',
        ),
        migrations.AddField(
            model_name='stock',
            name='previous_price',
            field=models.FloatField(default=0.0, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='history',
            field=jsonfield.fields.JSONField(default=__builtin__.dict),
            preserve_default=True,
        ),
    ]
