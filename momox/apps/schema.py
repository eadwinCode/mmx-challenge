from typing import Union, List

from django.core.paginator import Page
from django.db import models
from django.db.models import QuerySet
from ninja.schema import Schema


class BaseSchema(Schema):
    def apply(self, model_instance: models.Model, **kwargs):
        for attr, value in self.dict(**kwargs).items():
            setattr(model_instance, attr, value)
        return model_instance

    @classmethod
    def from_django(cls, model_instance: Union[models.Model, List[models.Model]], many=False):
        if many:
            if isinstance(model_instance, (QuerySet, list, Page)):
                return [cls.from_orm(model) for model in model_instance]
            raise Exception('model_instance must a queryset or list')
        return cls.from_orm(model_instance)
