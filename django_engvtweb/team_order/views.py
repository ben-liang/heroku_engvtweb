from haystack.views import FacetedSearchView
from haystack.query import SearchQuerySet
from django_engvtweb.cart.forms import *
from django.shortcuts import render
from models import *
#searchqueryset that is passed into view class
qbp_sqs = SearchQuerySet().order_by('category', 'brand').\
    facet('category', size=2000, order='term').\
    facet('brand', size=2000, order='term')

class QBPSearchView(FacetedSearchView):
    def build_page(self):
        (paginator,page) = super(QBPSearchView, self).build_page()

        #get objects being returned on this page to bind forms to
        this_page_results = page.object_list

        #now instantiate forms for each object in results
        forms = [AddToCartForm(initial={'object_id': res.object.id,
                                        'object_type': QbpPart.get_slug_name()})
                                        for res in this_page_results]

        #modify objects to add "cart_form" attr and reattach to page
        for i in range(len(forms)):
            setattr(this_page_results[i].object,'cart_form', forms[i])
        setattr(page, 'object_list',this_page_results)

        return (paginator, page)

def render_bike(request):
    return render(request, 'team_order/bike.html', {})

def render_stages(request):
    return render(request, 'team_order/stages.html', {})

