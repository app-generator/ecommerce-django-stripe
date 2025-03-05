# [Django & Stripe](https://blog.appseed.us/django-stripe-mini-ecommerce/) `Mini eCommerce`

**[Open-source eCommerce Starter](https://github.com/app-generator/rocket-ecommerce)** that loads the products from `JSON` files saved in the `templates directory` (no database required) and uses a decent UI for page styling - Powered by **Django & Stripe**.

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

<div align="center">
    <a href="https://app-generator.dev/product/rocket-ecommerce/django/">
        <img src="https://github-production-user-asset-6210df.s3.amazonaws.com/51070104/272178364-cbac6d97-b2dc-4d95-bab6-891f4ee7d84d.png"" width="64" height="64" alt="Rocket Icon">
    </a>
    <h1>
         Go PRO with 
        <a href="https://app-generator.dev/product/rocket-ecommerce/django/">
            Rocket eCommerce
        </a>
    </h1>
    <p>
        <strong>Django</strong> &bull; <strong>TailwindCSS</strong> &bull; <strong>Stripe</strong> &bull; <strong>Analytics</strong> &bull; <strong>Docker</strong> &bull; <strong>CI/CD</strong> &bull; <strong>Lifetime Updates</strong> &bull; <strong>Unlimited Projects</strong>
    </p>  
    <h3>     
        <a target="_blank" href="https://rocket-ecommerce.onrender.com">
            Demo
        </a>
        &nbsp; &bull; &nbsp;
        <a target="_blank" href="https://app-generator.dev/product/rocket-ecommerce/django/#pricing">
           Buy License
        </a>
    </h3>    
    <p>
        <strong>Once authenticated, the ADMIN (superuser) can import the products from Stripe and customize each one locally by adding properties like Images, Tags, Discount, .. etc.</strong>
        <br /> <br />
        The product comes with <strong>Docker</strong> and <a href="https://deploypro.dev/" target="_blank">CI/CD Support</a>
    </p>  
    <hr />
</div>

<br />

<div align="center">
  <img src="https://github.com/user-attachments/assets/3d3e4abc-3a4e-4ef2-8934-d55bc25942db" alt="Rocket eCommerce - Django Starter styled with Tailwind and Flowbite.">
</div>

<br />

## Features 

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
| ✅  | Active versioning and [support](https://appseed.us/support/) | [AppSeed](https://appseed.us/) |
| ✅  | [AWS, DO, Azure Deploy Assistance](https://deploypro.dev/)   | `DeployPRO` |

<br />
