__author__ = 'bliang'
from django.db import models
import pandas
from django.db.transaction import atomic

def removeNonAscii(s):
    if isinstance(s, basestring):
        return "".join(i for i in s if ord(i)<128)
    else:
        return s

class PartBrandOrCategory(models.Model):
    """
    Generic class for Brand or Category models for any type product
    """

    class Meta:
        ordering = ['name',]
        abstract = True
        unique_together = ('name',)

    name = models.CharField('name', max_length=32, null=False, blank=False)

    def __unicode__(self):
        return '%s' % self.name

    @classmethod
    def get_object_ids_map(cls):
        """
        get ids in dict to speed up bulk create of objects
        #this will avoid a new query for each row
        """
        values_qs = cls.objects.all().values()
        #make it easier to work with here
        values_dict = dict([(i['name'],i['id']) for i in values_qs])
        return values_dict

    @classmethod
    @atomic
    def bulk_create_from_series(cls,pandas_series):
        """
        Shortcut to bulk_create new dimensions from Pandas series, i.e. DF column.

        Returns a dict of {'name': object_id} for easy lookup in creating new
        parts objects.

        :param pandas_series: a Pandas series object, e.g. df['brand'] from DataFrame
        :return: dict
        """
        #now create brands
        unique_values = pandas_series.unique()
        brand_objs = [cls(name=removeNonAscii(k)) for k in unique_values]
        cls.objects.bulk_create(brand_objs)

    @classmethod
    @atomic
    def get_or_create_from_series(cls,pandas_series):
        """
        Shortcut to get_or_create new dimensions from Pandas series, i.e. DF column.

        Returns a dict of {'name': object_id} for easy lookup in creating new
        parts objects.

        Will be a lot slower for large series than bulk_create_and_get_from_series,
        but may be necessary to use this instead for data sets involving previously
        existing dimension values.

        :param pandas_series: a Pandas series object, e.g. df['brand'] from DataFrame
        :return: dict
        """
        #now create brands
        unique_values = pandas_series.unique()
        for val in unique_values:
            cls.objects.get_or_create(name=removeNonAscii(val))

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
    """
    Generic Part model to subclass.

    MUST specify 'brand' and 'category' fields in subclass as FK's
    to dimension models.
    """
    class Meta:
        abstract = True

    tstamp = models.DateTimeField('tstamp', auto_now_add=True)
    model_no = models.CharField('model_no',max_length=16, null=True, blank=True)
    name = models.CharField('name', max_length=32)
    description = models.CharField('description', max_length=64,null=True,blank=True)
    msrp = models.FloatField('msrp', null=True, blank=True)
    unit_price = models.FloatField('unit_price')

    def __unicode__(self):
        return '%s' % self.name

    @classmethod
    def get_slug_name(cls):
        """
        Used for purposes of storing content_type names to use with
        shopping cart, which can contain multiple types of objects
        """
        return cls.__name__.lower()

    @classmethod
    @atomic
    def bulk_create_from_csv(cls, filepath, brand=None, category=None):
        """
        Imports file for a single vendor's parts or bikes into Bike or OtherPart
        model.  File must be csv and have the following headers::

            brand (optional)
            category (optional)
            model_no (nullable)
            name
            description (nullable)
            msrp (nullable)
            unit_price

        Additionally, if only importing parts for one brand and/or category,
        can specify brand/category names as keyword args to avoid having to
        create a new file field just for category/brand.

        :param file: path to CSV file
        :param brand: brand object. NOTE: If not None, will OVERRIDE ALL brand values in file
        :param category: category object. NOTE: If not None, will OVERRIDE ALL brand values in file
        :return Queryset for new objects
        """
        #read data into dataframe to make things quick
        df = pandas.io.parsers.read_csv(filepath, header=0)
        df = df.fillna('None')

        #figure out how to handle brands based on file headers and
        #kwargs
        brand_id = None
        if brand is None:
            if 'brand' not in df.keys():
                raise KeyError('Field "brand" must be specified either in brand file field'
                               ' or brand kwarg')
            else:
                #if passed in as column, bulk_create and get object ids for object creation
                brand_model = cls.brand.field.related.parent_model
                brand_model.get_or_create_from_series(df['brand'])
                brand_ids = brand_model.get_object_ids_map()
        else:
            brand_id = brand.id

        category_id = None
        #do the same for category
        if category is None:
            if 'category' not in df.keys():
                raise KeyError('Field "category" must be specified either in brand file field'
                               ' or brand kwarg')
            else:
                #now get_or_create categories
                #first get category model
                category_model = cls.category.field.related.parent_model
                #call pre-defined method on category model to bulk_create_categories
                category_model.get_or_create_from_series(df['category'])
                category_ids = category_model.get_object_ids_map()
        else:
            category_id = category.id

        #now we're ready to bulk create the objects
        n = lambda v: None if v == 'None' else v
        #create
        parts_objs = []
        for i in range(0, len(df)):
            row = df.ix[i]
            part = cls(model_no=n(row.model_no),
                       name=n(removeNonAscii(row['name'])),
                       brand_id=(brand_id or brand_ids[n(removeNonAscii(row.brand))]),
                       category_id=(category_id or category_ids[n(row.category)]),
                       description=n(removeNonAscii(row.description)),
                       msrp=n(row.msrp),
                       unit_price=row.unit_price)
            parts_objs.append(part)
        #finally, bulk create all parts
        cls.objects.bulk_create(parts_objs)
        return parts_objs

## Bikes ##
class BikeBrand(PartBrandOrCategory):
    pass

class BikeCategory(PartBrandOrCategory):
    pass

class Bike(Part):
    brand = models.ForeignKey(BikeBrand)
    category = models.ForeignKey(BikeCategory)

## Other Parts ##
class OtherPartVendor(PartBrandOrCategory):
    pass

class OtherPartCategory(PartBrandOrCategory):
    pass

class OtherPart(Part):
    brand = models.ForeignKey(OtherPartVendor)
    category = models.ForeignKey(OtherPartCategory)
