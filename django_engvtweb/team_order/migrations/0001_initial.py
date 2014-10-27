# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QbpBrand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=64, verbose_name=b'brand')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QbpPart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tstamp', models.DateTimeField(auto_now_add=True, verbose_name=b'tstamp')),
                ('prodid', models.CharField(max_length=32, verbose_name=b'prod id')),
                ('UPC', models.BigIntegerField(null=True, verbose_name=b'upc', blank=True)),
                ('category', models.CharField(max_length=64, verbose_name=b'category')),
                ('model', models.CharField(max_length=32, verbose_name=b'model')),
                ('model_description', models.CharField(max_length=64, null=True, verbose_name=b'model_description', blank=True)),
                ('size', models.CharField(max_length=32, null=True, verbose_name=b'size', blank=True)),
                ('color', models.CharField(max_length=32, null=True, verbose_name=b'color', blank=True)),
                ('msrp', models.FloatField(verbose_name=b'msrp')),
                ('map', models.FloatField(verbose_name=b'map')),
                ('each_cost', models.FloatField(verbose_name=b'each cost')),
                ('manufacturer_prod', models.CharField(max_length=64, null=True, verbose_name=b'manufacturer_prod', blank=True)),
                ('coo', models.CharField(max_length=16, null=True, verbose_name=b'coo', blank=True)),
                ('discontinued', models.BooleanField()),
                ('uom', models.CharField(max_length=16, null=True, verbose_name=b'uom', blank=True)),
                ('weight', models.FloatField(verbose_name=b'weight')),
                ('length', models.FloatField(verbose_name=b'length')),
                ('width', models.FloatField(verbose_name=b'width')),
                ('height', models.FloatField(verbose_name=b'height')),
                ('ormd', models.BooleanField()),
                ('product_description', models.CharField(max_length=128, verbose_name=b'product_description')),
                ('replacement', models.CharField(max_length=64, null=True, verbose_name=b'replacement', blank=True)),
                ('substitute', models.CharField(max_length=64, null=True, verbose_name=b'substitute', blank=True)),
                ('brand', models.ForeignKey(to='QbpBrand')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
