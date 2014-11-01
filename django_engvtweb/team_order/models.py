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

    @classmethod
    def get_slug_name(cls):
        """
        Used for purposes of storing content_type names to use with
        shopping cart, which can contain multiple types of objects
        """
        return cls.__name__.lower()

class BikeBrand(models.Model):
    name = models.CharField('name', max_length=32)

class BikeCategory(models.Model):
    name = models.CharField('category', max_length=32)

class Bike(models.Model):
    tstamp = models.DateTimeField('tstamp', auto_now_add=True)
    brand = models.ForeignKey(BikeBrand)
    category = models.ForeignKey(BikeCategory)
    name = models.CharField('name', max_length=32)
    description = models.CharField('description', max_length=64)
    msrp = models.FloatField('msrp', null=True, blank=True)
    unit_price = models.FloatField('unit_price')

    @classmethod
    def get_slug_name(cls):
        """
        Used for purposes of storing content_type names to use with
        shopping cart, which can contain multiple types of objects
        """
        return cls.__name__.lower()

class OtherPartVendor(models.Model):
    name = models.CharField('name', max_length=32)

class OtherPartCategory(models.Model):
    name = models.CharField('name', max_length=32)

class OtherPart(models.Model):
    tstamp = models.DateTimeField('tstamp', auto_now_add=True)
    brand = models.ForeignKey(OtherPartVendor)
    category = models.ForeignKey(OtherPartCategory)
    model_no = models.CharField('model_no',max_length=16, null=True, blank=True)
    name = models.CharField('name',max_length=32)
    description = models.CharField('name',max_length=64, null=True, blank=True)
    msrp = models.FloatField('msrp', null=True, blank=True)
    unit_price = models.FloatField('unit_price')

    @classmethod
    def get_slug_name(cls):
        """
        Used for purposes of storing content_type names to use with
        shopping cart, which can contain multiple types of objects
        """
        return cls.__name__.lower()





