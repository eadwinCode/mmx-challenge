import logging
from typing import List, Dict, Union, Iterator
import xmltodict
from momox.order_processor.base_processor import OrderProcessor
from momox.order_processor.dto import ProcessorEmployeeDto, ProcessorOrderItemDto
from momox.order_processor.nhna_mock_meal_table import get_meal_id

logger = logging.getLogger()


class XMLOrderProcessor(OrderProcessor):
    def get_employees(self) -> Iterator[ProcessorEmployeeDto]:
        employees = self.data_dict.get('Employees')
        if isinstance(employees['Employee'], list):
            for employee in employees['Employee']:
                parsed_employee_data = self.parse_employee(data=employee)
                yield parsed_employee_data
            return
        parsed_employee_data = self.parse_employee(data=employees['Employee'])
        yield parsed_employee_data

    def parse_employee(self, *, data: Dict[str, Union[str, Dict[str, str]]]) -> ProcessorEmployeeDto:
        try:
            return ProcessorEmployeeDto(**data, orders=self.parse_order(data=data.get('Order')))
        except Exception as ex:
            logger.error(f'{self.__class__.__name__} - Parsing Employee Failed, exception:{ex}')
            raise ex

    @classmethod
    def parse_order(cls, *, data: str) -> List[ProcessorOrderItemDto]:
        try:
            orders = data.split(',')
            result = []
            for order in orders:
                amount, *others = tuple(order.strip().split(" "))
                meal = ' '.join(others)
                # Todo: Query nhna endpoint for meal_id
                meal_id = get_meal_id(meal)
                result.append(ProcessorOrderItemDto(
                    amount=int(amount[:-1].strip()), meal=meal, id=meal_id
                ))
            return result
        except Exception as ex:
            logger.error(f'{cls.__name__} - Parsing Order Failed, exception:{ex}')
            raise ex

    def __init__(self, data):
        self.data_dict: dict = xmltodict.parse(data)
