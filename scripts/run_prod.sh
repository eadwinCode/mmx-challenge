#!/usr/bin/env bash

# Script to run the Django server in a production environment

python manage.py collectstatic --no-input --clear
python manage.py migrate
gunicorn --bind :8001 --access-logfile - --error-logfile - momox.wsgi:application
