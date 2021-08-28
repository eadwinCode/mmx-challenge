import logging
from typing import Dict, List

import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail as django_send_mail


logger = logging.getLogger(__name__)


@shared_task(name="post_data_nhna_endpoint")
def post_data_nhna_endpoint(orders: List[Dict]):
    endpoint = getattr(settings, 'NHNA_ENDPOINT', None)
    if not endpoint:
        logger.error('NHNA_ENDPOINT Not Found in settings')
        raise Exception('NHNA_ENDPOINT Not Found in settings')

    logger.info(f'Request Order Received')
    response = requests.post(endpoint, json=orders)
    return str(response)
