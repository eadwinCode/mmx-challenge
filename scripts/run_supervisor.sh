#!/bin/bash

cp /var/app/supervisor/${supervisor_env}.conf /etc/supervisor/conf.d/
supervisord -n