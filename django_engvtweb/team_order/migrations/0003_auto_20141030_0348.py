# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0002_auto_20141025_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='qbpbrand',
            options={'ordering': ['brand']},
        ),
        migrations.RenameField(
            model_name='qbppart',
            old_name='each_cost',
            new_name='unit_price'
        ),
    ]
