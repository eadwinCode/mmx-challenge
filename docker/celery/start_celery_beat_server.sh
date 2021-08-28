#!/bin/sh

echo 'Starting celery beat'

celery -A momox beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
