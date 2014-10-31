__author__ = 'bliang'
from django.conf.urls import include, patterns, url
from haystack.forms import FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView
from views import *
from forms import *

urlpatterns = patterns('',
    url(r'^qbp/', QBPSearchView(form_class=QbpForm,
                                template='team_order/qbp.html',
                                searchqueryset=qbp_sqs), name='qbp'),
    url(r'^bike/', render_bike, name='bike'),
    url(r'^stages/', render_stages, name='stages'),
)