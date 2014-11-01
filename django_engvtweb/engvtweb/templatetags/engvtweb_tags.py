from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
register = template.Library()
#add template tags here


@register.inclusion_tag('include/jquery/jquery-js.html')
def include_jquery(version='2.1.1'):
    """
    Include jquery in your template

    :param str version: version of jquery to use
    :return: dict
    """
    return {'version': version}

@register.filter()
def currency(dollars):
    dollars = round(float(dollars), 2)
    return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])

@register.filter()
def to_int(float):
    return int(float)

@register.assignment_tag
def get_item(iterable, index):
    """
    Serves as proxy for iterable.__get_item__ method, allows you to
    retrieve item from an iterable by index in a template

    Registered as an assignment tag which allows you to store
    result as another template variable, so you can do stuff with it.

    Ex::

        {% get_item formset forloop.counter0 as form %}

    Here, you can access the n-th element of a formset inside of a template
    for loop, and store it as the template variable form.  Then, when you want
    to access the variable again, just call it like a normal template variable::

        {{ form.as_p }}

    """
    return iterable[index]