from typing import List
from pydantic import BaseModel as PydanticModel, Field
from momox.apps.employees.dto import EmployeeAddress
from momox.apps.orders.dto import MealOrderSchema


class NHNACustomerSchema(PydanticModel):
    name: str
    address: EmployeeAddress


class OrderNHNASchema(PydanticModel):
    customer: NHNACustomerSchema
    items: List[MealOrderSchema]


class UploadEmployeeOrdersSchema(PydanticModel):
    message: str
    posted_data: List[OrderNHNASchema]

    def serializer_for_task(self):
        return [item.json() for item in self.posted_data]
