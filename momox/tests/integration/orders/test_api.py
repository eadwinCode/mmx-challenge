from unittest.mock import patch

import pytest
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from ninja.testing import TestClient
from momox.api.order import router

TEST_FILE_PATH = '/tests'


@pytest.mark.django_db
class TestTokenAuthAPI:
    def test_upload_employees_orders_works(self):
        client = TestClient(router)

        with open(str(settings.BASE_DIR) + f"{TEST_FILE_PATH}/fixtures/employee_orders.xml", "rb") as fp:
            file = SimpleUploadedFile("test.txt", fp.read())
            with patch('momox.apps.orders.tasks.post_data_nhna_endpoint.delay') as celery_task_delay:
                response = client.post('/upload/employees-orders', FILES={"file": file})
                assert celery_task_delay.called is True

        response_json = response.json()
        assert response.status_code == 200
        assert 'Upload process was successful' in response_json['message']

    def test_upload_employees_orders_fails_for_invalid_data_upload(self):
        client = TestClient(router)

        with open(str(settings.BASE_DIR) + f"{TEST_FILE_PATH}/fixtures/employee_orders_invalid.xml", "rb") as fp:
            file = SimpleUploadedFile("test.txt", fp.read())
            with patch('momox.apps.orders.tasks.post_data_nhna_endpoint.delay') as celery_task_delay:
                response = client.post('/upload/employees-orders', FILES={"file": file})
                assert celery_task_delay.called is False

        response_json = response.json()
        assert response.status_code == 400
        assert 'Employees Order generation failed' in response_json['message']


