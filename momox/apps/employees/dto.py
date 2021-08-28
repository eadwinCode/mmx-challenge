from typing import Optional

from pydantic.types import UUID

from momox.apps.schema import BaseSchema


class EmployeeAddress(BaseSchema):
    street: str
    city: str
    postal_code: str


class Employee(BaseSchema):
    id: Optional[UUID]
    name: str
    address: EmployeeAddress
    is_attending: bool

