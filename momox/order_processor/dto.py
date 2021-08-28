from typing import List
from pydantic import BaseModel as PydanticModel, Field

from momox.apps.employees.dto import Employee, EmployeeAddress
from momox.apps.orders.dto import CreateMealOrderSchema


class ProcessorOrderItemDto(PydanticModel):
    amount: int
    meal: str
    id: int

    def convert_to_create_meal_schema(self):
        return CreateMealOrderSchema(**self.dict(), nhna_meal_id=self.id)


class ProcessorEmployeeAddressDto(PydanticModel):
    street: str = Field(..., alias='Street')
    city: str = Field(..., alias='City')
    postal_code: str = Field(..., alias='PostalCode')


class ProcessorEmployeeDto(PydanticModel):
    name: str = Field(..., alias='Name')
    address: ProcessorEmployeeAddressDto = Field(..., alias='Address')
    is_attending: bool = Field(..., alias='IsAttending')
    orders: List[ProcessorOrderItemDto]

    def convert_to_employee_scheme(self) -> Employee:
        address = EmployeeAddress(**self.address.dict())
        model_schema = Employee(**self.dict(exclude={'address'}), address=address)
        return model_schema
