# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0014_auto_20141104_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstocarts',
            name='tstamp',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 4, 23, 3, 7, 111267), auto_now_add=True),
            preserve_default=False,
        ),
    ]
