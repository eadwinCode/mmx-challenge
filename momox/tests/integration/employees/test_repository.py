import pytest

from momox.apps.employees.dto import Employee, EmployeeAddress
from momox.repositories.employee import EmployeeRepository

py_test_mark = pytest.mark.django_db


@py_test_mark
class TestEmployeeRepository:
    def test_get_employee_works(self, employee):
        employee_orm_schema = EmployeeRepository.get_employee(employee_id=employee.id)
        assert employee_orm_schema.json() == Employee.from_django(employee).json()

    def test_get_employee_by_name_works(self, employee):
        employee_orm_schema = EmployeeRepository.get_employee_by_name(name=employee.name)
        assert employee_orm_schema.json() == Employee.from_django(employee).json()

    def test_is_employee_registered_works(self, employee):
        assert EmployeeRepository.is_employee_registered(name=employee.name)
        assert not EmployeeRepository.is_employee_registered(name="Harman Kardon")

    def test_save_employee_works(self):
        employee_data = Employee(
            name="Harman Kardon", is_attending=True,
            address=EmployeeAddress(street="Anonymous", city="Anonymous", postal_code="52452")
        )
        assert EmployeeRepository.save_employee(employee_data)
        assert EmployeeRepository.is_employee_registered(name=employee_data.name)

