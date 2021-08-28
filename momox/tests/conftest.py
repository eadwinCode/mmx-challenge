import pytest
import os
import shutil
from random import random, randint
from django.test import Client
from momox.tests.integration.employees.factories import EmployeeFactory, EmployeeAddressFactory
from momox.tests.integration.orders.factories import MealOrderFactory


@pytest.fixture
def api_client():
    return Client()


@pytest.fixture
def employee():
    return EmployeeFactory()


@pytest.fixture
def meal_order(employee):
    return MealOrderFactory(employee=employee)


@pytest.fixture
def random_email():
    return "email{}@email.com".format(random())


@pytest.fixture
def random_username():
    return "username{}".format(random())


@pytest.fixture
def random_id(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def clean_up_file(settings):
    rmdir = str(settings.MEDIA_ROOT)
    shutil.rmtree(rmdir, ignore_errors=True)


@pytest.fixture(scope='session', autouse=True)
def test_clean_up():
    from django.conf import settings
    yield
    clean_up_file(settings)
