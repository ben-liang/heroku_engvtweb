# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0005_auto_20141101_1425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qbpbrand',
            options={'ordering': ['name']},
        ),
        migrations.RenameField(
            model_name='qbpbrand',
            old_name='brand',
            new_name='name',
        ),
    ]
