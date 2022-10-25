# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="products_index"),
    path('product/<str:slug>/', views.product_details, name='product_details'),
    path('load-product/', views.load_product_json, name='load_product'),
    path('create-product/', views.create_new_product, name='create_product'),
    path('update-product/<str:slug>/', views.update_product, name='update_product'),
    path('create-checkout-session/<str:slug>/', views.create_checkout_session, name="create-checkout-session"),
    path('success/', views.success, name="success"),
    path('cancelled/', views.cancelled, name="cancelled"),
    path('config/', views.get_publishable_key, name="config"),

    # pages
    path('presentation/', views.presentation, name="presentation"),
    path('about-us/', views.about_us, name="about_us"),
    path('contact-us/', views.contact_us, name="contact_us"),
    path('author/', views.author, name="author"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('page404/', views.page404, name="page404"),

    # blocks
    path('page-header/', views.page_header, name="page_header"),
    path('features/', views.features, name="features"),
    path('navbars/', views.navbars, name="navbars"),
    path('navtabs/', views.navtabs, name="navtabs"),
    path('paginations/', views.paginations, name="paginations"),
    path('input-areas/', views.input_areas, name="input_areas"),
    path('input-forms/', views.input_forms, name="input_forms"),
    path('alerts/', views.alerts, name="alerts"),
    path('modals/', views.modals, name="modals"),
    path('tooltips/', views.tooltips, name="tooltips"),
    path('buttons/', views.buttons, name="buttons"),
    path('avatars/', views.avatars, name="avatars"),
    path('dropdowns/', views.dropdowns, name="dropdowns"),
    path('toggles/', views.toggles, name="toggles"),
    path('breadcrumbs/', views.breadcrumbs, name="breadcrumbs"),
    path('badges/', views.badges, name="badges"),
    path('typography/', views.typography, name="typography"),
    path('progressbar/', views.progressbar, name="progressbar"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
