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
    if json.loads(obj)['img_main'].startswith("http"):
        return json.loads(obj)['img_main']
    else:
        return ""

@register.filter
def product_card_image(obj):
    if json.loads(obj)['img_card'].startswith('http'):
        return json.loads(obj)['img_card']
    else:
        return ""

@register.filter
def product_image1(obj):
    if json.loads(obj)['img_1'].startswith("http"):
        return json.loads(obj)['img_1']
    else:
        return ""

@register.filter
def product_image2(obj):
    if json.loads(obj)['img_2'].startswith('http'):
        return json.loads(obj)['img_2']
    else:
        return ""

@register.filter
def product_image3(obj):
    if json.loads(obj)['img_3'].startswith("http"):
        return json.loads(obj)['img_3']
    else:
        return ""


@register.filter
def product_slug(obj):
    name = json.loads(obj)['name']
    slug = name.lower().replace(' ', '-')
    return slug