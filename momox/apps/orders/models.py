from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel

# Create your models here.


class MealOrderORM(UUIDModel, TimeStampedModel):
    employee = models.ForeignKey(
        'employees.EmployeeORM', on_delete=models.CASCADE,
        related_name='orders', null=False
    )
    amount = models.IntegerField(null=False)
    nhna_meal_id = models.IntegerField(null=False)
    meal = models.CharField(max_length=50)

    def __repr__(self):
        return f'<MealOrderORM quantity:{self.amount}, meal: {self.meal}>'

    def __str__(self):
        return f'{self.employee.name} ordered {self.meal}'
