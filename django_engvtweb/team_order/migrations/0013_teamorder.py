# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team_order', '0012_auto_20141101_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tstamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'name')),
                ('active', models.BooleanField(default=True, verbose_name=b'active')),
                ('due_date', models.DateTimeField(verbose_name=b'due_date')),
                ('submitted_date', models.DateTimeField(null=True, verbose_name=b'submitted_date', blank=True)),
                ('administrator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
