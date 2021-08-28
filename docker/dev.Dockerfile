#################
# development Image
#################
FROM base
LABEL MAINTAINER="eadwinCode ezeudoh.tochukwu@gmail.com"
ENV DJANGO_SETTINGS_MODULE momox.settings.dev
RUN        apt-get -y update && apt-get -y install supervisor

COPY       test-requirements.txt /var/app/test-requirements.txt
RUN        pip install --no-cache-dir -r /var/app/test-requirements.txt

COPY       momox /var/app/momox
COPY       pytest.ini /var/app/pytest.ini
COPY       manage.py /var/app/manage.py
COPY       supervisor /var/app/supervisor

COPY       scripts/run_local.sh /var/app/run_local.sh
COPY       scripts/run_test.sh /var/app/run_test.sh
COPY       scripts/run_supervisor.sh /var/app/run_supervisor.sh

RUN        find /var/app/ -type f -iname "*.sh" -exec chmod +x {} \;
EXPOSE     8001
CMD        ["/var/app/run_supervisor.sh"]