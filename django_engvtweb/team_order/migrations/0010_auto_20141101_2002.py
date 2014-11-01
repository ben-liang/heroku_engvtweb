# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0009_auto_20141101_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikebrand',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'name'),
        ),
        migrations.AlterField(
            model_name='bikecategory',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'name'),
        ),
        migrations.AlterField(
            model_name='otherpartcategory',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'name'),
        ),
        migrations.AlterField(
            model_name='otherpartvendor',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'name'),
        ),
        migrations.AlterField(
            model_name='qbpbrand',
            name='name',
            field=models.CharField(max_length=64, verbose_name=b'name'),
        ),
    ]
