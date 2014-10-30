from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import *
from django_engvtweb.team_order.models import QbpPart
from changuito import CartProxy

#map of models to strings used in forms to reference
#each model.  Doing this just to avoid having to do an "eval(str)"
#in order to get the model class.

#Convention will be to just use the model name as a string when
#referencing it.

PRODUCT_MODELS = {
    QbpPart.__name__: QbpPart,
}

def add_item_to_shopping_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            object_type = form.cleaned_data['object_type']
            obj_id = form.cleaned_data['object_id']
            model = PRODUCT_MODELS[object_type]
            product = model.objects.get(id=obj_id)
            cart = request.cart
            cart.add(product, product.unit_price, quantity)
            return HttpResponseRedirect(reverse('cart:cart-add'))

def render_shopping_cart(request):
    return render(request, 'cart/index.html',dict(cart=CartProxy(request)))

