#!/bin/sh

set -e

# Wait for database running:
sleep 5
while [[ $(nc -z $db_host 5432 &> /dev/null; echo $?) -ne 0 ]]; do echo pod is not running;sleep 3; done

python manage.py collectstatic --noinput

gunicorn ecommerce.wsgi:application --bind :8000
