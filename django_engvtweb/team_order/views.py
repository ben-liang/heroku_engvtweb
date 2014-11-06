from haystack.views import FacetedSearchView
from haystack.query import SearchQuerySet
from django.views.generic import View, ListView
from django.shortcuts import render
from django_engvtweb.cart.forms import *
from django_engvtweb.team_order.forms import TeamOrderForm
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
                                        'object_type': QbpPart.__name__})
                 for res in this_page_results]

        #modify objects to add "cart_form" attr and reattach to page
        for i in range(len(forms)):
            setattr(this_page_results[i].object,'cart_form', forms[i])
        setattr(page, 'object_list',this_page_results)

        return (paginator, page)

class BikeList(ListView):

    model = Bike

    def get_queryset(self):
        return self.model.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        """
        Get AddToCart forms to render in-line with object list
        """
        context = super(BikeList, self).get_context_data(**kwargs)
        context['forms'] = AddToCartWithVariantForm.bind_to_object_list(self.get_queryset())
        return context

class OtherPartList(ListView):
    """
    Generic view for parts in OtherPart model.
    """
    model = OtherPart
    brand_name = None
    title = None

    def get_queryset(self):
        """
        Filters OtherParts for "active" objects with brand__name == brand_name.

        If no brand_name set, will return all active objects.

        Can set brand_name in call to self.as_view in urlconf. Ex::

            url(r'^stages', OtherPartList.as_view(brand_name='Stages'))

        Note that brand_name must be exact match for OtherPartBrand's name
        """
        if hasattr(self, 'brand_name'):
            return self.model.objects.filter(active=True, brand__name=self.brand_name)
        else:
            return self.model.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        """
        Get AddToCart forms to render in-line with object list
        """
        context = super(OtherPartList, self).get_context_data(**kwargs)
        forms = AddToCartWithVariantForm.bind_to_object_list(self.get_queryset())
        context['forms'] = forms

        #figure out what the hell the title of the page should be
        if self.title:
            context['title'] = self.title
        elif self.brand_name:
            context['title'] = self.brand_name
        else:
            context['title'] = 'All OtherParts'
        return context

class TeamOrderDetailsView(View):

    template = 'team_order/team_order_details.html'
    def get(self):
        pass

    def post(self):
        pass

