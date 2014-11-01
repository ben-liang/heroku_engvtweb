# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0007_auto_20141101_1540'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bikebrand',
            unique_together=set([('name',)]),
        ),
        migrations.AlterUniqueTogether(
            name='bikecategory',
            unique_together=set([('name',)]),
        ),
        migrations.AlterUniqueTogether(
            name='otherpartcategory',
            unique_together=set([('name',)]),
        ),
        migrations.AlterUniqueTogether(
            name='otherpartvendor',
            unique_together=set([('name',)]),
        ),
        migrations.AlterUniqueTogether(
            name='qbpbrand',
            unique_together=set([('name',)]),
        ),
    ]
