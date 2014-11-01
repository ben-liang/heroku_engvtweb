__author__ = 'bliang'
from django.contrib import admin
from .models import *

class QBPPartsAdmin(admin.ModelAdmin):
    list_display = ['prodid', 'category', 'brand', 'model_description',
                    'size','color','msrp','unit_price','product_description']
    date_hierarchy = 'tstamp'
    readonly_fields = ['prodid', 'category', 'brand', 'model_description',
                    'size','color','msrp','unit_price','product_description']
    search_fields = ['prodid', 'category', 'brand__brand', 'model_description',
                    'size','color','msrp','unit_price','product_description']
    list_filter = ['category','brand','size']

class QBPBrandsAdmin(admin.ModelAdmin):
    list_display = ['brand']
    search_fields = ['brand']
    readonly_fields = ['brand']

class BikeBrandsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class BikeAdmin(admin.ModelAdmin):
    list_display = ['brand','category','name','description','msrp','unit_price']
    search_fields = ['brand','category','name','description']
    list_filter = ['category','brand']

class OtherPartVendorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class OtherPartAdmin(admin.ModelAdmin):
    list_display = ['brand','category','name','description','msrp','unit_price']
    search_fields = ['brand','category','name','description']
    list_filter = ['category','brand']

admin.site.register(QbpPart,QBPPartsAdmin)
admin.site.register(QbpBrand,QBPBrandsAdmin)
admin.site.register(BikeBrand,BikeBrandsAdmin)
admin.site.register(Bike,BikeAdmin)
admin.site.register(OtherPartVendor,OtherPartVendorAdmin)
admin.site.register(OtherPart,OtherPartAdmin)
