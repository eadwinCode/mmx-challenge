#!/usr/bin/env bash

sleep 15

echo "Running migrations..."
python3 ./manage.py migrate

pytest ./momox/tests/