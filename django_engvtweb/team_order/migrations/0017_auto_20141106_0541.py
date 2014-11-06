# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0016_auto_20141106_0530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qbppart',
            old_name='product_description',
            new_name='description'
        ),
        migrations.AlterField(
            model_name='bike',
            name='prodid',
            field=models.CharField(max_length=16, null=True, verbose_name=b'prodid', blank=True),
        ),
        migrations.AlterField(
            model_name='otherpart',
            name='prodid',
            field=models.CharField(max_length=16, null=True, verbose_name=b'prodid', blank=True),
        ),
    ]
