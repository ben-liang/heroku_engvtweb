__author__ = 'bliang'
from django.db import models
import pandas
from utils import removeNonAscii

class PartBrandOrCategory(models.Model):

    class Meta:
        ordering = ['name',]
        abstract = True

    name = models.CharField('name', max_length=32, null=False, blank=False)

    def __unicode__(self):
        return '%s' % self.brand

    @classmethod
    def create_and_get_from_df_col(cls,pandas_series):
        #now create brands
        unique_values = pandas_series.unique()
        brand_objs = [cls(brand=removeNonAscii(k)) for k in unique_values]
        QbpBrand.objects.bulk_create(brand_objs)

        #get ids in dict to speed up bulk create of objects
        #this will avoid a new query for each row
        values_qs = cls.objects.all().values()
        #make it easier to work with here
        values_qs = dict([(i['brand'],i['id']) for i in values_qs])
        return values_qs

class QbpBrand(PartBrandOrCategory):
    pass

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

class Part(models.Model):

    class Meta:
        abstract = True

    tstamp = models.DateTimeField('tstamp', auto_now_add=True)
    model_no = models.CharField('model_no',max_length=16, null=True, blank=True)
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

    @classmethod
    def bulk_create_from_csv(cls, filepath, brand=None):
        """
        Imports file for a single vendor's parts or bikes into Bike or OtherPart
        model.  File must be csv and have headers:

        brand(optional)   category    model_no(optional) description msrp    unit_price

        :param file: path to file
        :param brand: string for brand name
        """
        #read data into dataframe to make things quick
        df = pandas.io.parsers.read_csv(filepath, header=0)
        df = df.fillna('None')

        if brand is None:
            if df['brand']:
                pass

        #now get_or_create categories
        unique_brands = df['category'].unique()
        brand_objs = [QbpBrand(name=removeNonAscii(k)) for k in unique_brands]
        QbpBrand.objects.bulk_create(brand_objs)

        n = lambda v: None if v == 'None' else v
        #create
        parts_objs = []
        for i in range(0, len(df)):
            row = df.ix[i]
            part = cls(model_no=n(row.model_no),
                       name=n(row.name),
                       brand=n(row.brand),
                       category=n(row.category),
                       description=removeNonAscii(n(row.description)),
                       msrp=n(row.msrp),
                       unit_price=row.unit_price)
            parts_objs.append(part)
        #finally, bulk create all parts
        cls.objects.bulk_create(parts_objs)


class BikeBrand(PartBrandOrCategory):
    pass

class BikeCategory(PartBrandOrCategory):
    pass

class Bike(Part):
    brand = models.ForeignKey(BikeBrand)
    category = models.ForeignKey(BikeCategory)

class OtherPartVendor(PartBrandOrCategory):
    pass

class OtherPartCategory(PartBrandOrCategory):
    pass

class OtherPart(Part):
    brand = models.ForeignKey(OtherPartVendor)
    category = models.ForeignKey(OtherPartCategory)