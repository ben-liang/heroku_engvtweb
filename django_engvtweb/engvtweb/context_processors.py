"""
Custom context processors to inject default template variables for all views.
"""
def shopping_cart(request):
    # try:
    cart = request.cart.cart
    return {'shopping_cart': cart}
    # except:
    #     return {}
