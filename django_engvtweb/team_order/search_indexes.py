__author__ = 'bliang'
from haystack import indexes
from models import *

class QbpPartIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    product_description = indexes.CharField(model_attr='product_description')
    brand = indexes.CharField(model_attr='brand', faceted=True, stored=True, indexed=False)
    prodid = indexes.CharField(model_attr='prodid', stored=True)
    category = indexes.CharField(model_attr='category', faceted=True, stored=True, indexed=False)
    model = indexes.CharField(model_attr='model')

    def get_model(self):
        return QbpPart
