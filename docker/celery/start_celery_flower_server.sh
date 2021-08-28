#!/bin/sh

echo 'Starting celery flower'

celery flower -A momox --address=0.0.0.0 --port=5555