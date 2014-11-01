# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team_order', '0003_auto_20141030_0348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tstamp', models.DateTimeField(auto_now_add=True, verbose_name=b'tstamp')),
                ('name', models.CharField(max_length=32, verbose_name=b'name')),
                ('description', models.CharField(max_length=64, verbose_name=b'description')),
                ('msrp', models.FloatField(null=True, verbose_name=b'msrp', blank=True)),
                ('unit_price', models.FloatField(verbose_name=b'unit_price')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BikeBrand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BikeCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OtherPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tstamp', models.DateTimeField(auto_now_add=True, verbose_name=b'tstamp')),
                ('model_no', models.CharField(max_length=16, null=True, verbose_name=b'model_no', blank=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'name')),
                ('description', models.CharField(max_length=64, null=True, verbose_name=b'name', blank=True)),
                ('msrp', models.FloatField(null=True, verbose_name=b'msrp', blank=True)),
                ('unit_price', models.FloatField(verbose_name=b'unit_price')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OtherPartCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OtherPartVendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='otherpart',
            name='brand',
            field=models.ForeignKey(to='team_order.OtherPartVendor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='otherpart',
            name='category',
            field=models.ForeignKey(to='team_order.OtherPartCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bike',
            name='brand',
            field=models.ForeignKey(to='team_order.BikeBrand'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bike',
            name='category',
            field=models.ForeignKey(to='team_order.BikeCategory'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='qbppart',
            name='unit_price',
            field=models.FloatField(verbose_name=b'unit_price'),
        ),
    ]
