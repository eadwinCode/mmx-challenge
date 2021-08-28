from pydantic import Field
from momox.apps.schema import BaseSchema


class MealOrderSchema(BaseSchema):
    amount: int
    id: int


class CreateMealOrderSchema(BaseSchema):
    amount: int
    nhna_meal_id: int = Field(..., alias='id')
    meal: str



