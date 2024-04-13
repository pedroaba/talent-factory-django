#!/usr/bin/env bash
until python test_connection.py; do
  echo "Database is unavailable"
  sleep 1
done

echo "Creating migrations"
python manage.py makemigrations

echo "Applying migrations"
python manage.py migrate

echo "Collecting static files"
python manage.py collectstatic --noinput

echo "Running application"
gunicorn talent_factory.wsgi:application --timeout 900 -w 17 -b :8000
