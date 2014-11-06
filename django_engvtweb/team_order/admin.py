__author__ = 'bliang'
from django.contrib import admin
from .models import *

class TeamOrderAdmin(admin.ModelAdmin):
    list_display = ['tstamp','name','active','due_date','submitted_date','administrator']
    date_hierarchy = 'tstamp'
    search_fields = ['name']
    list_filter = ['active','administrator']

class OrderToCartAdmin(admin.ModelAdmin):
    list_display = ['tstamp','team_order','cart']
    list_filter = ['team_order']
    search_fields = ['team_order','cart']

class QBPPartsAdmin(admin.ModelAdmin):
    list_display = ['prodid', 'category', 'brand', 'model_description',
                    'size','color','msrp','unit_price','description']
    date_hierarchy = 'tstamp'
    readonly_fields = ['prodid', 'category', 'brand', 'model_description',
                    'size','color','msrp','unit_price','description']
    search_fields = ['prodid', 'category', 'brand__brand', 'model_description',
                    'size','color','msrp','unit_price','description']
    list_filter = ['category','brand','size']

class QBPBrandsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    readonly_fields = ['name']

class BikeBrandsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class BikeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class BikeAdmin(admin.ModelAdmin):
    list_display = ['brand','category','name','description','msrp','unit_price','active']
    search_fields = ['brand','category','name','description']
    list_filter = ['category','brand','active']

class OtherPartVendorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class OtherPartCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class OtherPartAdmin(admin.ModelAdmin):
    list_display = ['brand','category','name','description','msrp','unit_price','active']
    search_fields = ['brand','category','name','description']
    list_filter = ['category','brand','active']

admin.site.register(TeamOrder,TeamOrderAdmin)
admin.site.register(OrdersToCarts,OrderToCartAdmin)
admin.site.register(QbpPart,QBPPartsAdmin)
admin.site.register(QbpBrand,QBPBrandsAdmin)
admin.site.register(BikeBrand,BikeBrandsAdmin)
admin.site.register(BikeCategory,BikeCategoryAdmin)
admin.site.register(Bike,BikeAdmin)
admin.site.register(OtherPartVendor,OtherPartVendorAdmin)
admin.site.register(OtherPartCategory,OtherPartCategoryAdmin)
admin.site.register(OtherPart,OtherPartAdmin)
