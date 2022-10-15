from django import template
from products.models import Product

register = template.Library()

@register.simple_tag
def sample_product_list():
    return Product.objects.all()[0:3]