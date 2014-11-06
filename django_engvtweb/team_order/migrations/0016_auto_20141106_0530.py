# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0015_orderstocarts_tstamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='model_no',
            new_name='prodid'
        ),
        migrations.RenameField(
            model_name='otherpart',
            old_name='model_no',
            new_name='prodid'
        ),
    ]
