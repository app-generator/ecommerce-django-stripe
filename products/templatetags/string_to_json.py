import json
from django import template

register = template.Library()

@register.filter
def product_name(obj):
    return json.loads(obj)['name']


@register.filter
def product_slug(obj):
    name = json.loads(obj)['name']
    slug = name.lower().replace(' ', '-')
    return slug