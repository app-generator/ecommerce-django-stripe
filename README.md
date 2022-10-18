# Django & Stripe `Mini eCommerce`

Open-source mini `eCommerce` project that loads the products from `JSON` files saved in the [templates](https://github.com/app-generator/sample-django-stripe/tree/main/products/templates/products) directory (no database required) and uses a decent UI for page styling - Powered by **Django**.

<br />

> Features:

- ✅ [Soft UI Design](https://www.creative-tim.com/product/soft-ui-design-system?AFFILIATE=128200) (Free Version) by `Creative-Tim`
- ✅ Powered by `Django` & `Stripe`
- ✅ NO database, NO authentication
- ✅ Automatic Products discovery from [templates\products](./products/templates/products) directory 
  - [JSON Format](./products/templates/products/product-air-zoom-pegasus.json) (sample) 

<br />

## ✨ Quick Start

<br />

> 👉 Create `.env` using provided `env.sample`

 Add `.env` file in your projects root directory and add the following credentials

```
DEBUG=True
SECRET_KEY=
STRIPE_SECRET_KEY=
STRIPE_PUBLISHABLE_KEY=
DOMAIN_URL=
```

<br />

> 👉 Install dependencies

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br /> 

> 👉 Migrate DB & Start the APP

```bash
$ python manage.py migrate
$ python manage.py runserver
```

Visit `http://localhost:8000` in your browser. The app should be up & running.

<br />

> 👉 Access the products and initiate a payment

**IMPORTANT**: Make sure your Stripe account is running in `TEST Mode` and Use Test CC provided by Stripe:

- **CC Number**: `4242 4242 4242 4242`
- Any data for the rest of the fields  

<br />

## ✨ Create a new Product

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


> Sample product page generated for [Air ZOOM Pegasus](./products/templates/products/product-air-zoom-pegasus.json), assets loaded from [here](./products/static/products/product-air-zoom-pegasus)

<br />

![Django Stripe Sample - Air ZOOM Pegasus (sample Product](https://user-images.githubusercontent.com/51070104/152586940-2f3b31fb-f067-487a-98ca-26d9e1936514.png)

<br />

## ✨ Codebase structure

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

## ✨ Credits & Links

- [Django Framework](https://www.djangoproject.com/) - The official website
- [Stripe Dev Tools](https://stripe.com/docs/development) - official docs

<br />

---
**Django Stripe Sample** - Free sample provided by [AppSeed](https://appseed.us).
