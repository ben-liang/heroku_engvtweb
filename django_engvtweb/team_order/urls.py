__author__ = 'bliang'
from django.conf.urls import patterns, url
from views import *
from forms import *

urlpatterns = patterns('',
    url(r'^qbp/', QBPSearchView(form_class=QbpForm,
                                template='team_order/qbp.html',
                                searchqueryset=qbp_sqs), name='qbp'),
    url(r'^bike/', BikeList.as_view(), name='bike'),
    url(r'^stages/', OtherPartList.as_view(brand_name='Stages',title='Stages Powermeters'), name='stages'),
    url(r'^team-order-details/', TeamOrderDetailsView.as_view(), name='team-order-details'),
    url(r'^send-order-details/', handle_email_form, name='send-order-details')
)