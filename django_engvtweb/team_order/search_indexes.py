__author__ = 'bliang'
from haystack import indexes
from models import *

class QbpPartIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    product_description = indexes.CharField(model_attr='product_description')
    brand = indexes.CharField(model_attr='brand')
    prodid = indexes.CharField(model_attr='prodid')
    category = indexes.CharField(model_attr='category')
    model = indexes.CharField(model_attr='model')

    def get_model(self):
        return QbpPart
