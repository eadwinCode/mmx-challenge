############
# Base Image
############
FROM python:3.6-slim AS base
LABEL MAINTAINER="eadwinCode ezeudoh.tochukwu@gmail.com"

RUN mkdir    /var/app
WORKDIR      /var/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /var/app/requirements.txt

RUN pip install --no-cache-dir -r /var/app/requirements.txt

# Add celery commands
RUN mkdir -p /var/celery
ADD ./docker/celery/start_celery_server.sh /var/celery
ADD ./docker/celery/start_celery_beat_server.sh /var/celery
ADD ./docker/celery/start_celery_flower_server.sh /var/celery

RUN   find /var/celery/ -type f -iname "*.sh" -exec chmod +x {} \;
RUN adduser --disabled-password celery


