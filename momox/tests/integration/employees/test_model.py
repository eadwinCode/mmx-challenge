import pytest
from momox.tests.integration.employees.factories import EmployeeFactory

py_test_mark = pytest.mark.django_db


class TestEmployeeORMModel:
    @py_test_mark
    def test_model_works(self):
        employee = EmployeeFactory()
        assert employee.is_attending

    @py_test_mark
    def test_model_constraint_works(self):
        with pytest.raises(Exception) as ex:
            EmployeeFactory(name='')
            assert 'NOT NULL constraint failed' in str(ex)
            EmployeeFactory(is_attending='')
            assert 'NOT NULL constraint failed' in str(ex)
