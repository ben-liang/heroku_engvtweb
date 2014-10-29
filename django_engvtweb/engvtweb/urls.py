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
    url(r'^team_order/', include('django_engvtweb.team_order.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls))
)
