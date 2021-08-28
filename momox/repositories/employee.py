import logging
from typing import Union

from django.db import transaction

from momox.apps.employees.dto import Employee
from momox.apps.employees.models import EmployeeORM, EmployeeAddressORM
from momox.utils.custom_exceptions import EntityDoesNotExist


logger = logging.getLogger()


class EmployeeRepository:
    @classmethod
    def get_employee(cls, employee_id: str) -> Employee:
        employee = EmployeeORM.objects.filter(id=employee_id).select_related('address').first()
        if not employee:
            raise EntityDoesNotExist('Model Does not exist')
        return Employee.from_django(employee)

    @classmethod
    def get_employee_by_name(cls, name: str) -> Union[Employee, None]:
        employee = EmployeeORM.objects.filter(name=name).select_related('address').first()
        if not employee:
            return None
        return Employee.from_django(employee)

    @classmethod
    def is_employee_registered(cls, name: str) -> bool:
        return EmployeeORM.objects.filter(name=name).exists()

    @classmethod
    def save_employee(cls, employee: Employee) -> str:
        try:
            employee_exist = cls.get_employee_by_name(name=employee.name)
            if employee_exist:
                return employee_exist.id

            with transaction.atomic():
                employee_orm_address = EmployeeAddressORM()
                employee.address.apply(employee_orm_address)
                employee_orm_address.save()
                employee_orm = EmployeeORM(
                    name=employee.name, is_attending=employee.is_attending, address=employee_orm_address
                )
                employee_orm.save()
                return str(employee_orm.id)
        except Exception as ex:
            logger.info(f'Saving Employee failed: exception: {str(ex)}')
            raise ex
