from django.db import models
from model_utils.models import UUIDModel, TimeStampedModel
# Create your models here.


class EmployeeAddressORM(UUIDModel, TimeStampedModel):
    street = models.CharField(null=False, max_length=150)
    city = models.CharField(null=False, max_length=150)
    postal_code = models.CharField(max_length=150, null=False)

    def __repr__(self):
        return f'<EmployeeAddressORM street:{self.street}, city:{self.city}, postalCode:{self.postal_code}>'

    def __str__(self):
        return f'EmployeeAddressORM: {self.employee.name}'


class EmployeeORM(UUIDModel, TimeStampedModel):
    name = models.CharField(null=False, max_length=150)
    is_attending = models.BooleanField(default=True, null=False)
    address = models.OneToOneField(EmployeeAddressORM, on_delete=models.DO_NOTHING, related_name='employee')

    def __repr__(self):
        return f'<EmployeeORM name:{self.name}, is_attending:{self.is_attending}>'

    def __str__(self):
        return f'EmployeeORM: {self.name}'

