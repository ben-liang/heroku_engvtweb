# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qbppart',
            name='discontinued',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='qbppart',
            name='ormd',
            field=models.BooleanField(default=False),
        ),
    ]
