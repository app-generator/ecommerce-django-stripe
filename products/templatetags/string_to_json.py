import json
from django import template

register = template.Library()

@register.filter
def product_name(obj):
    return json.loads(obj)['name']

@register.filter
def product_price(obj):
    return json.loads(obj)['price']

@register.filter
def product_description(obj):
    return json.loads(obj)['full_description']

@register.filter
def product_info(obj):
    return json.loads(obj)['info']

@register.filter
def product_main_image(obj):
    return json.loads(obj)['img_main']

@register.filter
def product_card_image(obj):
    return json.loads(obj)['img_card']

@register.filter
def product_image1(obj):
    return json.loads(obj)['img_1']

@register.filter
def product_image2(obj):
    return json.loads(obj)['img_2']

@register.filter
def product_image3(obj):
    return json.loads(obj)['img_3']


@register.filter
def product_slug(obj):
    name = json.loads(obj)['name']
    slug = name.lower().replace(' ', '-')
    return slug