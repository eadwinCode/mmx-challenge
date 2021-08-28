#################
# Furnistore production Image
#################
FROM base
LABEL MAINTAINER="eadwinCode ezeudoh.tochukwu@gmail.com"

ENV        DJANGO_SETTINGS_MODULE furniturestore.settings.prod
RUN        apt-get -y update && apt-get -y install supervisor
RUN        pip install gevent==21.1.2 psycogreen

COPY       momox /var/app/momox
COPY       pytest.ini /var/app/pytest.ini
COPY       manage.py /var/app/manage.py
COPY       supervisor /var/app/supervisor

COPY       scripts/run_prod.sh /var/app/run_prod.sh
COPY       scripts/run_test.sh /var/app/run_test.sh
COPY       scripts/run_supervisor.sh /var/app/run_supervisor.sh

RUN        find /var/app/ -type f -iname "*.sh" -exec chmod +x {} \;

EXPOSE     8001
CMD        ["/var/app/run_supervisor.sh"]