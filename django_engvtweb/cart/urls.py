from django.conf.urls import include, patterns, url
from views import *

urlpatterns = patterns('',
    url(r'^$', render_shopping_cart, name='cart'),
    url(r'^add/', add_item_to_shopping_cart, name='cart-add'),
    url(r'^remove/(?P<item_id>\d+)/$', remove_item, name='remove-item')
)