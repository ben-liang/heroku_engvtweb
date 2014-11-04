# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changuito', '0002_item_variant'),
        ('team_order', '0013_teamorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersToCarts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cart', models.ForeignKey(to='changuito.Cart')),
                ('team_order', models.ForeignKey(to='team_order.TeamOrder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='teamorder',
            name='carts',
            field=models.ManyToManyField(to='changuito.Cart', through='team_order.OrdersToCarts'),
            preserve_default=True,
        ),
    ]
