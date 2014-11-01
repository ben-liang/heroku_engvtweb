from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from forms import *
from django_engvtweb.team_order.models import QbpPart
from changuito import CartProxy

#map of models to strings used in forms to reference
#each model.  Doing this just to avoid having to do an "eval(str)"
#in order to get the model class.

#Convention will be to just use the lowercased model name as a string when
#referencing it.

PRODUCT_MODELS = {
    QbpPart.get_slug_name(): QbpPart,
}

def add_item_to_shopping_cart(request):
    """
    Handles addition of items to the shopping cart. Call from any product page
    as POST from an AddToCart form.

    :param request:
    :return: HttpResponseRedirect to cart
    """

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = int(form.cleaned_data['quantity'])
            object_type = form.cleaned_data['object_type']
            obj_id = form.cleaned_data['object_id']
            model = PRODUCT_MODELS[object_type]
            product = model.objects.get(id=obj_id)
            cart = request.cart
            cart.add(product, product.unit_price, quantity)
            return HttpResponseRedirect(reverse('cart:cart'))
    else:
        return Http404()

def render_shopping_cart(request):
    """

    :param request:
    :return:
    """
    if request.method == 'POST':
        pass
    else:
        cart = request.cart
        initial_data = [{'object_id': item.object_id,
                         'object_type': item.content_type.model,
                         'quantity': int(item.quantity)} for item in cart]
        formset = CartFormset(initial=initial_data)
        item_prices = [item.total_price for item in cart]
        total = sum(item_prices)
        return render(request, 'cart/index.html',
                      dict(cart=CartProxy(request), total=total, formset=formset))

