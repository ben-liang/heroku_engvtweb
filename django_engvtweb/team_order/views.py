from haystack.views import FacetedSearchView
from haystack.query import SearchQuerySet
import pandas
from django.views.generic import View, ListView
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from changuito.models import Item
from django_engvtweb.cart.forms import *
from django_engvtweb.team_order.forms import TeamOrderForm, EmailOrderForm
# from django_engvtweb.team_order.mail import

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

    template_name = 'team_order/team_order_details.html'
    group_by = None

    @staticmethod
    def get_all_order_items(team_order):
        """
        Get all items and carts in a query-efficient manner to avoid round trips.

        B/c of model structure it's difficult to write a Django query using built-in manager
        methods that don't result in hundreds of queries.  This does all of the prefetching
        items from the DB manually, and then effective joins in Python.

        :param TeamOrder team_order: TeamOrder object
        :return: pandas.DataFrame object containing all item details
        """
        carts = team_order.carts.all()
        related_fields = ['content_type','cart__user']
        items = Item.objects.filter(cart__in=carts).prefetch_related(*related_fields).all()
        content_ids = items.values('content_type','object_id')

        #do some ugly pre-fetching of items in order to minimize DB round trips
        # when DF is created
        contents_dict = {}
        all_models = [Bike, OtherPart, QbpPart]
        for model in all_models:
            #this is very hacky
            mname = model.__name__.lower()
            ctype = ContentType.objects.get(model=mname)
            ctype_id = ctype.id
            #get list of all object IDs for this content type
            object_ids = map(lambda f: f['object_id'],
                             filter(lambda f: f['content_type'] == ctype_id,content_ids))
            contents_dict[ctype] = ctype.get_all_objects_for_this_type(id__in=object_ids).\
                prefetch_related('brand').values('id','prodid','description','brand__name')

        temp = [None]*len(items)
        for i in range(0, len(items)):
            item = items[i]
            #get product details from content_dict
            product_dict = filter(lambda f: f['id'] == item.object_id,
                                  contents_dict[item.content_type])[0]
            d = {'user': ' '.join([item.cart.user.first_name,
                                   item.cart.user.last_name]),
                 'quantity': item.quantity,
                 'prodid': product_dict['prodid'],
                 'description': product_dict['description'],
                 'content_type': item.content_type.model,
                 'brand': product_dict['brand__name'],
                 'variant': item.variant,
                 'unit_price': item.unit_price,
                 'total_price': item.total_price}
            temp[i] = d
        df = pandas.DataFrame(temp)
        return df

    @staticmethod
    def group_by_ctype_and_brand(df):

        filled = df.fillna('null')
        #split out DFs by content_type (model)
        grouped_by_ctype = filled.groupby('content_type')
        ctype_dfs = {}
        for name, group in grouped_by_ctype:
            #within each content type, group by brand
            cdf = group.reset_index()
            brand_dfs = {}
            grouped_by_brand = cdf.groupby('brand')
            for bname, bgroup in grouped_by_brand:
                bdf = bgroup.reindex()
                brand_dfs[bname] = bdf.groupby(
                    ['prodid','description','variant']).sum().\
                    reset_index().to_dict('records')
            ctype_dfs[name] = brand_dfs
        return ctype_dfs

    @staticmethod
    def group_by_user(df):
        filled = df.fillna('null')
        grouped = filled.groupby('user')
        user_dict = {}
        for name, group in grouped:
            user_dict[name] = group.reset_index().to_dict('records')
        return user_dict

    def get(self, request):
        form = TeamOrderForm()
        return render(request, self.template_name, {'form': form, 'order_items': {}})

    def post(self, request):
        form = TeamOrderForm(request.POST)
        if form.is_valid():
            df = self.get_all_order_items(form.cleaned_data['team_order'])
            df_dict = self.group_by_ctype_and_brand(df)
            user_dict = self.group_by_user(df)
            return render(request, self.template_name, {'form': form, 'order_items': df_dict, 'user_items': user_dict})

# def handle_email_form(request):
#     if request.method == 'POST':
#         form = EmailOrderForm(request.POST)
#         if form.is_valid():
#             email_address = form.cleaned_data['email']
