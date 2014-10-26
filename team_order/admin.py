__author__ = 'bliang'
from django.contrib import admin
from .models import *

class QBPPartsAdmin(admin.ModelAdmin):
    list_display = ['prodid', 'category', 'brand', 'model_description',
                    'size','color','msrp','each_cost','product_description']
    date_hierarchy = 'tstamp'
    readonly_fields = ['prodid', 'category', 'brand', 'model_description',
                    'size','color','msrp','each_cost','product_description']
    search_fields = ['prodid', 'category', 'brand__brand', 'model_description',
                    'size','color','msrp','each_cost','product_description']
    list_filter = ['category','brand','size']

class QBPBrandsAdmin(admin.ModelAdmin):
    list_display = ['brand']
    search_fields = ['brand']
    readonly_fields = ['brand']

admin.site.register(QbpPart,QBPPartsAdmin)
admin.site.register(QbpBrand,QBPBrandsAdmin)