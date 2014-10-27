from django.conf.urls import patterns, include, url
from django.contrib import admin
from shop import urls as shop_urls

admin.autodiscover()

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    # url(r'^db', hello.views.db, name='db'),
    url(r'^grappelli/', include('grappelli.urls')),
    (r'^shop/', include(shop_urls)),
    url(r'^admin/', include(admin.site.urls)),

)
