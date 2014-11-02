from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    # url(r'^db', hello.views.db, name='db'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^team_order/', include('django_engvtweb.team_order.urls', namespace='team_order')),
    url(r'^cart/', include('django_engvtweb.cart.urls', namespace='cart')),
    url(r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls'))
)
