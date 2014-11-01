# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0006_auto_20141101_1533'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bikebrand',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='bikecategory',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='otherpartcategory',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='otherpartvendor',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='bikecategory',
            name='name',
            field=models.CharField(max_length=32, verbose_name=b'name'),
        ),
        migrations.AlterField(
            model_name='qbpbrand',
            name='name',
            field=models.CharField(max_length=32, verbose_name=b'name'),
        ),
    ]
