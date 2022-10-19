# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, fnmatch, json
from core.settings import BASE_DIR

class Product:
    name     = ''
    price    = 0
    currency = ''
    info     = ''
    short_description = ''
    full_description = ''
    slug     = '' 

def get_templates_dir():
    return os.path.join(BASE_DIR, 'products/templates' )

def get_products_dir():
    return os.path.join(BASE_DIR, 'products/templates', 'products' )

def get_product_path( aSlug ):
    return os.path.join(BASE_DIR, 'products/templates', 'products', aSlug )

def get_files( aPath, ext='html' ):
    matches = []
    for root, dirnames, filenames in os.walk( aPath ):
        for filename in fnmatch.filter(filenames, '*.'+ ext):
            item = os.path.join(root, filename)
            matches.append( item )
    return matches

def get_product( ):
    return get_files( get_products_dir(), 'json' )

def get_slug( aPath, aExt='json' ):
    if aPath:
        head, tail = os.path.split( aPath ) # get file name
        return tail.replace('.' + aExt, '') # remove extension
    return None

def load_json_product( aJSONPath ): 
    f = open(aJSONPath, 'r')
    if not f:
        return None   
    
    # Read Product Info    
    data = json.load( f )

    return data

def load_product( aJSONPath ): 
    f = open(aJSONPath, 'r')
    if not f:
        return None   
    
    # Read Product Info    
    data = json.load( f )
    
    if not data:
        return None 

    product = Product()

    product.name  = data["name"] 
    product.info  = data["info"]
    product.price = int( data["price"] )
    product.short_description = data["short_description"]
    product.full_description  = data["full_description"]
    product.slug  = get_slug( aJSONPath )

    return product

def load_product_by_slug( aSlug ):
    aJSONPath = get_product_path( aSlug + '.json' )
    return load_product( aJSONPath )
