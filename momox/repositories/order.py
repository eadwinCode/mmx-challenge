import logging
from typing import List

from django.db import transaction

from momox.apps.orders.dto import MealOrderSchema, CreateMealOrderSchema
from momox.apps.orders.models import MealOrderORM
from momox.utils.custom_exceptions import EntityDoesNotExist

logger = logging.getLogger()


class OrderRepository:
    @classmethod
    def get_order(cls, meal_order_id: str) -> MealOrderSchema:
        meal_order = MealOrderORM.objects.filter(id=meal_order_id).select_related('employee').first()
        if not meal_order:
            raise EntityDoesNotExist('Model Does not exist')
        return MealOrderSchema.from_django(meal_order)

    @classmethod
    def order_exist(cls, meal_order_id: str) -> MealOrderSchema:
        return MealOrderORM.objects.filter(id=meal_order_id).exists()

    @classmethod
    def get_employee_orders(cls, employee_id: str) -> List[MealOrderSchema]:
        meal_orders = MealOrderORM.objects.filter(employee__id=employee_id).all()
        return [MealOrderSchema(id=item.nhna_meal_id, amount=item.amount) for item in meal_orders]

    @classmethod
    def get_employee_orders_by_name(cls, name: str) -> List[MealOrderSchema]:
        meal_orders = MealOrderORM.objects.filter(employee__name__exact=name).all()
        return [MealOrderSchema(id=item.nhna_meal_id, amount=item.amount) for item in meal_orders]

    @classmethod
    def save_order(cls, employee_id: str, order: CreateMealOrderSchema) -> MealOrderSchema:
        try:
            with transaction.atomic():
                meal_orm = MealOrderORM(employee_id=employee_id)
                order.apply(model_instance=meal_orm)
                meal_orm.save()
                return MealOrderSchema(id=meal_orm.nhna_meal_id, amount=meal_orm.amount)
        except Exception as ex:
            logger.info(f'Saving MealOrder failed: exception: {str(ex)}')
            raise ex

    @classmethod
    def save_bulk_orders(cls, employee_id: str, orders: List[CreateMealOrderSchema]) -> List[MealOrderSchema]:
        try:
            saved_orders = []
            for order in orders:
                saved_orders.append(cls.save_order(employee_id=employee_id, order=order))
            return saved_orders
        except Exception as ex:
            logger.info(f'Saving MealOrder failed: exception: {str(ex)}')
            raise ex
