# [Django & Stripe](https://blog.appseed.us/django-stripe-mini-ecommerce/) `Mini eCommerce`

**[Open-source eCommerce Starter](https://github.com/app-generator/rocket-ecommerce)** that loads the products from `JSON` files saved in the `templates directory` (no database required) and uses a decent UI for page styling - Powered by **Django & Stripe**.

<br />

## Features

> `Have questions?` Contact **[Support](https://appseed.us/support/)** (Email & Discord) provided by **AppSeed**

| Free Version                          | [PRO Version](https://github.com/app-generator/rocket-ecommerce) - 🛒 **[$49](https://appseed.gumroad.com/l/rocket-ecommerce)** | [Custom Development](https://appseed.us/custom-development/) |  
| --------------------------------------| --------------------------------------| --------------------------------------|
| ✓ Stack: **Django**, `Bootstrap`      | ✅ Stack: **Django**, `TailwindCSS`              | **Everything in PRO**, plus:         |
| ✓ Payments: **Stripe**                | ✅ Payments: **Stripe**                          | ✅ **1mo Custom Development**       | 
| ✓ Minimal Bootstrap Design            | ✅ **Stripe Products Import**                    | ✅ **Team**: PM, Developer, Tester  |
| ✓ No Database                         | ✅ **Local Products Customization**              | ✅ Weekly Sprints                   |
| -                                     | ✅ **Categories**, TAGS                          | ✅ Technical SPECS                  |
| -                                     | ✅ Multi-product **Checkout**                    | ✅ Documentation                    |
| -                                     | ✅ **Discounts Page**                            | ✅ **30 days Delivery Warranty**    |
| -                                     | ✅ **Analytics**                                 | -                                    |
| -                                     | ✅ **Transactions Tracking**                     |  -                                   |
| -                                     | ✅ **Zero Configuration**                        |  -                                   |
| -                                     | ✅ **Deployment** Assistance                     |  -                                   |
| -                                     | ✅ **PRO Support** - [Email & Discord](https://appseed.us/support/) |  -                |
| ------------------------------------  | ------------------------------------              | ------------------------------------|
| -                                     | 🚀 [LIVE Demo](https://rocket-ecommerce.onrender.com/) | 🛒 `Order`: **[$3,999](https://appseed.gumroad.com/l/rocket-package)** (GUMROAD) |  

<br />

![Django & Stripe Mini eCommerce - Open-Source Starter provided by AppSeed.](https://user-images.githubusercontent.com/51070104/196479738-be20d203-df44-47ce-a124-d3ed426ef622.jpg)

<br />

## Manual Build

> 👉 **Step 1** - Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/ecommerce-django-stripe.git
$ cd ecommerce-django-stripe
```

<br />

> 👉 **Step 2** - Create `.env` using provided `env.sample`

 Add `.env` file in your projects root directory and add the following credentials

```
DEBUG=True
SECRET_KEY=
STRIPE_SECRET_KEY=
STRIPE_PUBLISHABLE_KEY=
DOMAIN_URL=
```

<br />

> 👉 **Step 3** - Install dependencies

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br /> 

> 👉 **Step 4** - Migrate DB & Start the APP

```bash
$ python manage.py migrate
$ python manage.py runserver
```

Visit `http://localhost:8000` in your browser. The app should be up & running.

<br />

> 👉 **Step 5** - Access the products and initiate a payment

**IMPORTANT**: Make sure your Stripe account is running in `TEST Mode` and Use Test CC provided by Stripe:

- **CC Number**: `4242 4242 4242 4242`
- Any data for the rest of the fields  

<br />

## Create a new Product

- Go to `products/templates/products` directory
- Create a new `JSON` file with data:
  - `name`: Used in product page & Cards
  - `price`: Used for payment
  - `currency`: Used for payment
  - `info`: used in cards 
  - `short_description`: used in product page
  - `full_description`: used in product page
- Create Media Files
  - Go to `products/static/products` 
  - Create a directory using the same name as for `JSON` file
    - Create `card.jpg`: 500x335px
    - Create `cover.jpg`: 2100x1400px
- Start or refresh the app
  - The new product should be listed in the `home` page
  - Product page is available at address:
    - `http://127.0.0.1:8000/product/<SLUG>/` where the SLUG is the name of the JSON file 


<br />

## Load and create product from stripe


- Go to `Create Product` route in `Products` dropdown [You must be a superuser] 
- On the left side there should be a button `Get Products From Stripe` this button will pull all the products associated with the stripe account. [demo](./products/static/products/demo/load-stripe-product.png)
  - There will be product list, you can create a product by clicking the `Create` button. [demo](./products/static/products/demo/create-product.png)
- On the right side you will see the local product list and a button `Edit`.
  - You can edit a product from here. [ID is not editable] [demo](./products/static/products/demo/edit-product.png)
  
<br />

> Sample product page generated for [Air ZOOM Pegasus](./products/templates/products/product-air-zoom-pegasus.json), assets loaded from [here](./products/static/products/product-air-zoom-pegasus)

<br />

![Django Stripe Sample - Air ZOOM Pegasus (sample Product](https://user-images.githubusercontent.com/51070104/152586940-2f3b31fb-f067-487a-98ca-26d9e1936514.png)

<br />

## Codebase structure

The project has a simple structure, represented as bellow:

```bash
< PROJECT ROOT >
   |
   |-- products/__init__.py
   |-- products/
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/
   |    |    |
   |    |    |-- includes/                 # Page chunks, components
   |    |    |    |-- navigation.html      # Top bar
   |    |    |    |-- sidebar.html         # Left sidebar
   |    |    |    |-- scripts.html         # JS scripts common to all pages
   |    |    |    |-- footer.html          # The common footer
   |    |    |
   |    |    |-- layouts/                  # App Layouts (the master pages)
   |    |    |    |-- base.html            # Used by common pages like index, UI
   |    |    |    |-- base-fullscreen.html # Used by auth pages (login, register)
   |    |    |
   |    |    |-- products/                        # Define your products here
   |    |    |    |-- nike-goalkeeper-match.json  # Sample product
   |
   |-- requirements.txt
   |
   |-- run.py
   |
   |-- ************************************************************************
```

<br />

## Credits & Links

- [Django Framework](https://www.djangoproject.com/) - The official website
- [Stripe Dev Tools](https://stripe.com/docs/development) - official docs

<br />

---
**[Django & Stripe](https://blog.appseed.us/django-stripe-mini-ecommerce/) Mini eCommerce** - Free sample provided by [AppSeed](https://appseed.us).
