"""
A mock to NHNA Meal table.
"""


class MealNotFoundException(Exception):
    pass


meal_table = {
    'Kebap': 13,
    'Pizza Quattro Formaggi': 3,
    'Fried Chicken': 23,
    'Caesar Salad': 42
}


def get_meal_id(meal: str) -> int:
    meal_id = meal_table.get(meal)
    if not meal_id:
        raise MealNotFoundException('Meal not found')
    return meal_id
