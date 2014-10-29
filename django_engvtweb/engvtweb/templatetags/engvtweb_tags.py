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