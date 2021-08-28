import pytest

from momox.apps.orders.dto import MealOrderSchema, CreateMealOrderSchema
from momox.repositories.order import OrderRepository

py_test_mark = pytest.mark.django_db


@py_test_mark
class TestEmployeeRepository:
    def test_get_order_works(self, meal_order):
        orm_orm_schema = OrderRepository.get_order(meal_order_id=meal_order.id)
        assert orm_orm_schema.json() == MealOrderSchema.from_django(meal_order).json()

    def test_get_get_employee_orders_works(self, meal_order):
        orm_orm_schema = OrderRepository.get_employee_orders(employee_id=meal_order.employee_id)
        assert orm_orm_schema[0].json() == MealOrderSchema(id=meal_order.nhna_meal_id, amount=meal_order.amount).json()

    def test_get_employee_orders_by_name_works(self, meal_order, employee):
        orm_orm_schema = OrderRepository.get_employee_orders_by_name(name=employee.name)
        assert orm_orm_schema[0].json() == MealOrderSchema(id=meal_order.nhna_meal_id, amount=meal_order.amount).json()

    def test_save_order_works(self, employee):
        order_data = CreateMealOrderSchema(amount=2, id=23, meal='Yam & Egg Stew')
        order_orm_schema = OrderRepository.save_order(employee_id=employee.id, order=order_data)
        assert order_orm_schema
        assert order_orm_schema.amount == order_data.amount
        assert order_orm_schema.id == order_data.nhna_meal_id

    def test_save_bulk_orders_works(self,employee):
        orders_data = [
            CreateMealOrderSchema(amount=2, id=23, meal='Yam & Egg Stew'),
            CreateMealOrderSchema(amount=2, id=45, meal='Rice & Egg Stew')
        ]
        order_orm_schemas = OrderRepository.save_bulk_orders(employee_id=employee.id, orders=orders_data)
        assert len(order_orm_schemas) == len(orders_data)
        for order_orm_schema, order_data in zip(order_orm_schemas, orders_data):
            assert order_orm_schema.amount == order_data.amount
            assert order_orm_schema.id == order_data.nhna_meal_id
