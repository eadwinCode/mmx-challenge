import logging
from ninja import Router, File
from ninja.files import UploadedFile

from momox.api.order.schemas import UploadEmployeeOrdersSchema, OrderNHNASchema, NHNACustomerSchema
from momox.apps.orders.tasks import post_data_nhna_endpoint
from momox.order_processor.xml_processor import XMLOrderProcessor
from momox.repositories.employee import EmployeeRepository
from momox.repositories.order import OrderRepository

router = Router()
logger = logging.getLogger()


@router.post('/upload/employees-orders', response=UploadEmployeeOrdersSchema)
def employees_order(request, file: UploadedFile = File(...)):
    try:
        data = file.read()
        order_processor = XMLOrderProcessor(data=data)
        employees = order_processor.get_employees()
        orders = []
        for employee in employees:
            if EmployeeRepository.is_employee_registered(employee.name):
                items = OrderRepository.get_employee_orders_by_name(employee.name)
                orders.append(OrderNHNASchema(customer=NHNACustomerSchema(**employee.dict()), items=items))
                continue

            customer_id = EmployeeRepository.save_employee(employee.convert_to_employee_scheme())
            items = OrderRepository.save_bulk_orders(
                employee_id=customer_id,
                orders=[item.convert_to_create_meal_schema() for item in employee.orders]
            )
            orders.append(OrderNHNASchema(customer=NHNACustomerSchema(**employee.dict()), items=items))

        response = UploadEmployeeOrdersSchema(message="Upload process was successful", posted_data=orders)
        # post to NHNA api on background
        post_data_nhna_endpoint.delay(orders=response.serializer_for_task())
        return response
    except Exception as ex:
        logger.error(f'Employees Order generation failed: exception={ex}')
        return router.api.create_response(request, data=dict(message='Employees Order generation failed'), status=400)
