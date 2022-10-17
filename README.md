# [Django & Stripe]() `Mini eCommerce`


> Features:

- ✅ Powered by `Django` & `Stripe`
- ✅ UI Kit: **Soft UI Kit** (Free Version) by **Creative-Tim**
- ✅ `Deployment`: **Docker**

<br />

## ✨ Create .env
<br />

> 👉 Add `.env` file in your projects root directory and add the following credentials

```
DEBUG=True
SECRET_KEY=
STRIPE_SECRET_KEY=
STRIPE_PUBLISHABLE_KEY=
DOMAIN_URL=
```

## ✨ Start the app in `Docker`


<br />

> 👉 Start the APP in `Docker`

```bash
$ docker-compose up --build 
```

Visit `http://localhost:8000` or `http://127.0.0.1:8000/` in your browser. The app should be up & running.

<br />

## ✨ Quick Start

<br />

> 👉 Install dependencies

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />


## ✨ Create a new Product

```bash
$ python manage.py migrate
$ python manage.py createsuperuser
```
- Go to `http://127.0.0.1:8000/admin/` and login with the superuser credentials.
- Create a new Product with data:
  - `name`: Used in product page & Cards
  - `image`: Used for preview products
  - `cover_image`: Used for preview products cover image
  - `price`: Used for payment
  - `currency`: Used for payment
  - `info`: Used in cards 
  - `short_description`: Used in product page
  - `full_description`: Used in product page
  - `is_featured`: Used for featured product
  
<br />

> 👉 Start the App

```bash
$ python manage.py runserver
```

<br />

> 👉 Access the products and initiate a payment

**IMPORTANT**: Make sure your Stripe account is running in `TEST Mode` and Use Test CC provided by Stripe:

- **CC Number**: `4242 4242 4242 4242`
- Any data for the rest of the fields  

<br />


> Sample product page generated for [Air ZOOM Pegasus]()

<br />

![Flask Stripe Sample - Air ZOOM Pegasus (sample Product](https://user-images.githubusercontent.com/51070104/152586940-2f3b31fb-f067-487a-98ca-26d9e1936514.png)

<br />
