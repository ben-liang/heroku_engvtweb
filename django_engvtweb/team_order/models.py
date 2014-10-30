__author__ = 'bliang'
from django.db import models

class QbpBrand(models.Model):
    brand = models.CharField('brand', max_length=64, null=False, blank=False)

    def __unicode__(self):
        return '%s' % self.brand

    class Meta:
        ordering = ['brand',]

# Create your models here.
class QbpPart(models.Model):
    class Meta:
        pass

    tstamp = models.DateTimeField('tstamp', auto_now_add=True)
    prodid = models.CharField('prod id', max_length=32)
    UPC = models.BigIntegerField('upc', null=True, blank=True)
    category =  models.CharField('category', max_length=64)
    brand = models.ForeignKey(QbpBrand)
    model = models.CharField('model', max_length=32)
    model_description = models.CharField('model_description', max_length=64,
                                         null=True, blank=True)
    size = models.CharField('size', max_length=32, null=True, blank=True)
    color = models.CharField('color', max_length=32, null=True, blank=True)
    msrp = models.FloatField('msrp')
    map = models.FloatField('map')
    unit_price = models.FloatField('unit_price')
    manufacturer_prod = models.CharField('manufacturer_prod', max_length=64,
                                         null=True, blank=True)
    coo =  models.CharField('coo', max_length=16, null=True, blank=True)
    discontinued = models.BooleanField(default=False)
    uom = models.CharField('uom', max_length=16, null=True, blank=True)
    weight = models.FloatField('weight')
    length = models.FloatField('length')
    width = models.FloatField('width')
    height = models.FloatField('height')
    ormd = models.BooleanField(default=False)
    product_description = models.CharField('product_description', max_length=128)
    replacement = models.CharField('replacement', max_length=64, null=True, blank=True)
    substitute = models.CharField('substitute', max_length=64, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.product_description
