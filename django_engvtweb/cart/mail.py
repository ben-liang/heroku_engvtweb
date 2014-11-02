from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django_engvtweb import SITE_NAME
from tabulate import tabulate

HTML_ORDER_CONFIRMATION_TEMPLATE = get_template('email/order_confirmation.html')
TEXT_ORDER_CONFIRMATION_TEMPLATE = get_template('email/order_confirmation.txt')

def tabulate_cart(cart):
    items = cart.item_set.all()
    rows = []
    for item in items:
        try:
            name = item.product.name
        except AttributeError:
            name = item.product.product_description
        price = '$%s' % round(item.total_price,2)
        quantity = int(item.quantity)
        l = [name,quantity, price]
        rows.append(l)
    rows.append(['Total',int(cart.total_quantity()), '%s' % round(cart.total_price(), 2)])
    headers = ['Product', 'Quantity', 'Price']
    return unicode(tabulate(rows, headers=headers))

def send_order_confirmation(cart, user, time, html_template=HTML_ORDER_CONFIRMATION_TEMPLATE,
                            text_template=TEXT_ORDER_CONFIRMATION_TEMPLATE, subject=None):
    d = {'order_number': cart.id,
         'username': user.username,
         'tstamp': time.strftime("%A, %B %d %Y %H:%M:%S"),
         'cart_items': cart.item_set.all(),
         'cart': cart,
         'item_table': tabulate_cart(cart)}
    mail_context = Context(d)
    html_content = html_template.render(mail_context)
    text_content = text_template.render(mail_context)
    if subject is None:
        subject = '%s Order Confirmation: Order %s' % (SITE_NAME, cart.id)
    sent = send_mail(subject,
                     text_content,
                     from_email='oleg@engvtweb.com',
                     recipient_list=[user.email],
                     html_message=html_content)
    return sent

def test():
    from django.contrib.auth.models import User
    from changuito.models import Cart
    t = datetime.utcnow()
    user = User.objects.get(id=1)
    cart = Cart.objects.get(id=16)
    send_order_confirmation(cart, user, t)