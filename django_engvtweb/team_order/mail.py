from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django_engvtweb import SITE_NAME
from tabulate import tabulate

def tabulate_cart(cart):
    """
    Renders unicode tabulation of cart items.
    """
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

# def send_order_confirmation(order, user, subject=None):
#
#     html_template = get_template('email/order_summary.html')
#     text_template = get_template('email/order_summary')
#
#     mail_context = Context(d)
#     html_content = html_template.render(mail_context)
#     text_content = text_template.render(mail_context)
#     if subject is None:
#         subject = '%s Order Confirmation: Order %s' % (SITE_NAME, cart.id)
#     sent = send_mail(subject,
#                      text_content,
#                      from_email='oleg@engvtweb.com',
#                      recipient_list=[user.email],
#                      html_message=html_content)
#     return sent
