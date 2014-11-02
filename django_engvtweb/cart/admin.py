__author__ = 'bliang'
from django.contrib import admin
from changuito.models import *

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'creation_date', 'checked_out','total_price']
    date_hierarchy = 'creation_date'
    ordering = ['-creation_date']
    readonly_fields = ['user', 'creation_date', 'checked_out','total_price']
    search_fields = ['user', 'creation_date', 'checked_out']
    list_filter = ['user', 'checked_out']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'quantity', 'unit_price','total_price','content_type','get_product',
                    'variant']
    ordering = ['cart']
    search_fields = ['cart', 'content_type', 'object_id','get_product']
    list_filter = ['cart']

admin.site.register(Cart,CartAdmin)
admin.site.register(Item,ItemAdmin)