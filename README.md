# Django & Stripe `Mini eCommerce`

**Open-source eCommerce Starter** that loads the products from `JSON` files saved in the `templates directory` (no database required) and uses a decent UI for page styling - Powered by **Django & Stripe**.

- [Django mini eCommerce](https://github.com/app-generator/ecommerce-django-stripe) sources (this repo)
- [Rocket eCommerce](https://app-generator.dev/product/rocket-ecommerce/django/) - **PRO Version**
  - ✅ Stripe Integration
  - ✅ Checkout, Discounts Page
  - ✅ Tags, Categories
  - ✅ Analytics
  - ✅ Generated Sitemap 

<br />

## Manual Build

> 👉 Download the code from the GH repository (using `GIT`) 

```bash
$ git clone https://github.com/app-generator/ecommerce-django-stripe.git
$ cd ecommerce-django-stripe
```

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

## Load and create product from Stripe

- Go to `Create Product` route in `Products` dropdown [You must be a superuser] 
- On the left side there should be a button `Get Products From Stripe` this button will pull all the products associated with the stripe account. [demo](./products/static/products/demo/load-stripe-product.png)
  - There will be product list, you can create a product by clicking the `Create` button. [demo](./products/static/products/demo/create-product.png)
- On the right side you will see the local product list and a button `Edit`.
  - You can edit a product from here. [ID is not editable] [demo](./products/static/products/demo/edit-product.png)
  
<br />

> Sample product page generated for [Air ZOOM Pegasus](./products/templates/products/product-air-zoom-pegasus.json), assets loaded from [here](./products/static/products/product-air-zoom-pegasus)

<br />

## Need More? Go PRO with [Rocket eCommerce](https://app-generator.dev/product/rocket-ecommerce/django/)

Production-ready eCommerce CMS integrated with Stripe, Analytics, Discounts Page, Docker and CI/CD support - Actively supported by [App-Generator](https://app-generator.dev/).

| Status | Item | info | 
| --- | --- | --- |
| ✅ | Stack | Django, Tailwind, React |
| ✅ | Payments | Stripe |
| ✅ | Categories | YES |
| ✅ | Tags | YES |
| ✅ | Checkout | YES |
| ✅ | Discounts Page | YES |
| ✅ | Products Import | Stripe |
| ✅ | Products Local Customization | YES |
| ✅ | Analitycs | Weekly, Monthly, Year `Sales` |
| ✅ | Transactions Tracking | YES |
| ✅ | Docker | YES |
| ✅ | CI/CD | Render |

![Rocket eCommerce - Production-ready eCommerce CMS integrated with Stripe, Analytics, Discounts Page, Docker and CI/CD support.](https://github.com/user-attachments/assets/5db5841f-6802-4dfa-8ce7-46cf14435c5a)

<br />

---
Django & Stripe `Mini eCommerce` - Open-source eCommerce Starter provided by [App-Generator](https://app-generator.dev/).
