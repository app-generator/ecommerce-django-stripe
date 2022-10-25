# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import json
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
import stripe
from products.utils import get_product, Product, load_product, load_product_by_slug, load_json_product, load_product_by_id
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from stripe_python import get_products

stripe.api_key = getattr(settings, 'STRIPE_SECRET_KEY')

STRIPE_KEY = getattr(settings, 'STRIPE_SECRET_KEY')
OUTPUT_FILE = 'products/templates/products/products.json' 

def index(request):
    # Collect Products
    products = []
    featured_product = None
    
    # Scan all JSONs in `templates/products`
    for aJsonPath in get_product():  
        if 'featured.json' in aJsonPath:
            continue

        # Load the product info from JSON
        product = load_product( aJsonPath )
        
        # Is Valid? Save the object
        if product:     
            products.append( product )

    context = {
        'featured': load_product_by_slug('featured'),
        'products': products
    }
    return render(request, 'ecommerce/index.html', context)

def product_details(request, slug):
    product = load_product_by_slug( slug )
    STRIPE_IS_ACTIVE = getattr(settings, 'STRIPE_IS_ACTIVE')

    context = { 
        'product': product,
        'STRIPE_IS_ACTIVE': STRIPE_IS_ACTIVE
     }
    return render(request, 'ecommerce/template.html', context)

def get_publishable_key(request):
    stripe_config = {"publicKey": getattr(settings, 'STRIPE_PUBLISHABLE_KEY')}
    return JsonResponse(stripe_config)

def success(request):
    return render(request, "ecommerce/payment-success.html")

def cancelled(request):
    return render(request, "ecommerce/payment-cancelled.html")

def create_checkout_session(request, slug):
    product = load_product_by_slug( slug )
    domain_url = getattr(settings, 'DOMAIN_URL')
    stripe.api_key = getattr(settings, 'STRIPE_SECRET_KEY')

    try:
        # Create new Checkout Session for the order
        # Other optional params include:
        # [billing_address_collection] - to display billing address details on the page
        # [customer] - if you have an existing Stripe Customer ID
        # [payment_intent_data] - lets capture the payment later
        # [customer_email] - lets you prefill the email input in the form
        # For full details see https:#stripe.com/docs/api/checkout/sessions/create

        # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=domain_url + "cancelled",
            payment_method_types=["card"],
            mode="payment",
            line_items=[
                {
                    "name": product.name,
                    "quantity": 1,
                    "currency": product.currency,
                    "amount": int(float(product.price) * 100),
                },
            ],
        )
        return JsonResponse({"sessionId": checkout_session["id"]})
    except Exception as e:
        return JsonResponse(error=str(e)), 403

@staff_member_required
def load_product_json(request):
    json_data = []

    # load stripe product
    if request.method == "POST":
        products = stripe.Product.list(expand = ['data.default_price'])
        productdict = []
        for product in products:
            dict= {}
            dict['id'] = product['id']
            dict['name'] = product['name']
            dict['price'] = product["default_price"]["unit_amount"]/100
            dict['currency'] = product["default_price"]["currency"]
            dict['full_description'] = product["description"]
            dict['info'] = product["description"][0:30]

            for index, image in enumerate(product['images']):
                dict['img_main'] = image

            dict['img_card'] = ''
            dict['img_1'] = ''
            dict['img_2'] = ''
            dict['img_3'] = ''

            productdict.append(dict)
        
        for product in productdict:
            json_product = json.dumps( product, indent=4, separators=(',', ': ') )
            json_data.append(json_product)

    # load local product
    local_products = []
    for aJsonPath in get_product():  
        if 'featured.json' in aJsonPath:
            continue
        local_json = load_json_product(aJsonPath)
        local_products.append(json.dumps( local_json, indent=4, separators=(',', ': ') ))
    
    context = {
        'productdict': json_data,
        'local_products': local_products
    }
    return render(request, 'ecommerce/create-product.html', context)


@staff_member_required
def create_new_product(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        name = json.loads(product)['name']
        slug = name.lower().replace(' ', '-')

        try:
            products = load_product_by_slug( slug )
            if products:
                return redirect('/load-product')
        except:
            outputFile = f'products/templates/products/{slug}.json'
            with open(outputFile, "w") as outfile: 
                outfile.write( product )
                outfile.close()
            return redirect('/load-product')
    else:
        return redirect('/load-product')


@staff_member_required
def update_product(request, slug):
    if request.method == 'POST':
        product = request.POST.get('product')
        id = json.loads(product)['id']
        name = json.loads(product)['name']

        try:
            products = load_product_by_slug( slug )
            if (products.id == id) and (products.name == name):
                outputFile = f'products/templates/products/{slug}.json'
                with open(outputFile, "r+") as outfile:
                    outfile.seek(0)
                    outfile.write(product)
                    outfile.truncate()
                return redirect('/load-product')
            else:
                messages.error(request, "You can't update product id or name!")
                return redirect('/load-product')
        except:
            messages.error(request, "You can't update product id or name!")
            return redirect('/load-product')  
    else:
        return redirect('/load-product')


# pages

def presentation(request):
    return render(request, 'pages/presentation.html')

def about_us(request):
    return render(request, 'pages/page-about-us.html')

def contact_us(request):
    return render(request, 'pages/page-contact-us.html')

def author(request):
    return render(request, 'pages/page-author.html')

def signin(request):
    return render(request, 'pages/page-sign-in.html')

def signup(request):
    return render(request, 'pages/page-sign-up.html')

def page404(request):
    return render(request, 'pages/page-404.html')

# blocks

def page_header(request):
    return render(request, 'pages/page-sections-hero-sections.html')

def features(request):
    return render(request, 'pages/page-sections-features.html')

def navbars(request):
    return render(request, 'pages/navigation-navbars.html')

def navtabs(request):
    return render(request, 'pages/navigation-nav-tabs.html')

def paginations(request):
    return render(request, 'pages/navigation-pagination.html')

def input_areas(request):
    return render(request, 'pages/input-areas-inputs.html')

def input_forms(request):
    return render(request, 'pages/input-areas-forms.html')

def alerts(request):
    return render(request, 'pages/attention-catchers-alerts.html')

def modals(request):
    return render(request, 'pages/attention-catchers-modals.html')

def tooltips(request):
    return render(request, 'pages/attention-catchers-tooltips-popovers.html')

def buttons(request):
    return render(request, 'pages/elements-buttons.html')

def avatars(request):
    return render(request, 'pages/elements-avatars.html')

def dropdowns(request):
    return render(request, 'pages/elements-dropdowns.html')

def toggles(request):
    return render(request, 'pages/elements-toggles.html')

def breadcrumbs(request):
    return render(request, 'pages/elements-breadcrumbs.html')

def badges(request):
    return render(request, 'pages/elements-badges.html')

def typography(request):
    return render(request, 'pages/elements-typography.html')

def progressbar(request):
    return render(request, 'pages/elements-progress-bars.html')
