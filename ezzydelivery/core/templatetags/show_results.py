from random import choice
from django import template

register = template.Library()


@register.inclusion_tag('core/profile.html')
def show_results(msg=5):
    choices = {'seller': 'Seller', 'driver': 'Driver'}
    return {'choices': choices}
