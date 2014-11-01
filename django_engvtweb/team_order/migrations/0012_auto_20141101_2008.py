# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0011_auto_20141101_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='otherpart',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
