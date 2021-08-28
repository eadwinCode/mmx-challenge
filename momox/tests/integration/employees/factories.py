import factory

from momox.apps.employees.models import EmployeeORM, EmployeeAddressORM


class EmployeeAddressFactory(factory.DjangoModelFactory):
    street = factory.Sequence(lambda n: "street_{0}".format(n+1))
    city = factory.Sequence(lambda n: "city_{0}".format(n+1))
    postal_code = factory.Sequence(lambda n: "postal_code_{0}".format(n+1))

    class Meta:
        model = EmployeeAddressORM


class EmployeeFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: "employee_{0}".format(n+1))
    is_attending = True
    address = factory.SubFactory(EmployeeAddressFactory)

    class Meta:
        model = EmployeeORM
