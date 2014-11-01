# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0008_auto_20141101_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='description',
            field=models.CharField(max_length=64, null=True, verbose_name=b'description', blank=True),
        ),
        migrations.AlterField(
            model_name='otherpart',
            name='description',
            field=models.CharField(max_length=64, null=True, verbose_name=b'description', blank=True),
        ),
    ]
