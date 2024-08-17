#!/bin/sh

echo "Apply database migrations"
python3 manage.py makemigrations
python3 manage.py migrate

echo "Creating superuser"
python3 manage.py createsuperuser --noinput --email "$DJANGO_SUPERUSER_EMAIL" --username "$DJANGO_SUPERUSER_USERNAME"

exec "$@"