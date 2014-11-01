# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0010_auto_20141101_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'name'),
        ),
        migrations.AlterField(
            model_name='otherpart',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'name'),
        ),
    ]
