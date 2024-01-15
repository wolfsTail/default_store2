from django.utils.http import urlencode
from django import template

from goods.models import Categories


register = template.Library()

@register.simple_tag()
def tag_categories():
    """
    Returns all categories.
    """
    return Categories.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    """
    Returns a URL-encoded string of the query parameters after updating them with the provided keyword arguments.
    
    Parameters:
        context (dict): The context dictionary containing the request object.
        **kwargs: Keyword arguments representing the query parameters to update.
        
    Returns:
        str: A URL-encoded string of the updated query parameters.
    """
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
