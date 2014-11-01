# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0004_auto_20141101_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='model_no',
            field=models.CharField(max_length=16, null=True, verbose_name=b'model_no', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='otherpart',
            name='description',
            field=models.CharField(max_length=64, verbose_name=b'description'),
        ),
    ]
