#!/bin/sh

echo 'Starting Celery'

celery worker -l info --app momox --uid celery