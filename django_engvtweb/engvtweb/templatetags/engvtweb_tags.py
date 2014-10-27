from django import template
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