import factory
from momox.apps.orders.models import MealOrderORM


class MealOrderFactory(factory.DjangoModelFactory):
    amount = factory.Sequence(lambda n: n+1*2)
    nhna_meal_id = factory.Sequence(lambda n: n+1+2)
    meal = factory.Sequence(lambda n: "meal_{0}".format(n+1))

    class Meta:
        model = MealOrderORM
