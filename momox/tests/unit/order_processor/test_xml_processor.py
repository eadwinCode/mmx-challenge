import pytest
import logging
from pydantic import ValidationError

from momox.order_processor.dto import ProcessorEmployeeDto, ProcessorOrderItemDto, ProcessorEmployeeAddressDto
from momox.order_processor.xml_processor import XMLOrderProcessor

logger = logging.getLogger()


working_data = """
<Employees>
    <Employee>
        <Name>Arielle Hassle</Name>
        <Address>
            <Street>Hard Road 13</Street>
            <City>Old York</City>
            <PostalCode>98765</PostalCode>
        </Address>
        <IsAttending>true</IsAttending>
        <Order>1x Fried Chicken, 1x Caesar Salad</Order>
    </Employee>
</Employees>
"""


failing_employee_address_data = """
<Employee>
    <Name>Arielle Hassle</Name>
    <Address>
        <Street>Hard Road 13</Street>
        <City>Old York</City>
    </Address>
    <IsAttending>true</IsAttending>
    <Order>1x Fried Chicken, 1x Caesar Salad</Order>
</Employee>
"""

failing_employee_data = """
<Employee>
    <Name>Arielle Hassle</Name>
    <Address>
        <Street>Hard Road 13</Street>
        <City>Old York</City>
        <PostalCode>98765</PostalCode>
    </Address>
    <Order>1x Fried Chicken, 1x Caesar Salad</Order>
</Employee>
"""

failing_order_data = """
<Order>1xCaesar Salad</Order>
"""

working_order_data = """
<Order>1x Caesar Salad, 1x Caesar Salad, 1x Caesar Salad</Order>
"""

failing_meal_table_order_data = """
<Order>1x Jollof Rice Chicken</Order>
"""


class TestXMLProcessor:
    def test_xml_processor_works(self):
        order_processor = XMLOrderProcessor(data=working_data)
        sample = ProcessorEmployeeDto(
            Name='Arielle Hassle',
            IsAttending=True,
            Address=ProcessorEmployeeAddressDto(
                Street="Hard Road 13", City="Old York", PostalCode='98765'
            ),
            orders=[
                ProcessorOrderItemDto(amount=1, id=23, meal='Fried Chicken'),
                ProcessorOrderItemDto(amount=1, id=42, meal='Caesar Salad'),
            ]
        )
        employees = [item for item in order_processor.get_employees()]
        assert len(employees) == 1
        logger.error(employees[0].json())
        assert employees[0].json() == sample.json()

    def test_xml_processor_parse_employee_fails_for_invalid_address_data(self):
        order_processor = XMLOrderProcessor(data=failing_employee_address_data)
        with pytest.raises(ValidationError) as ex:
            order_processor.parse_employee(data=order_processor.data_dict.get('Employee'))
        assert 'PostalCode' in str(ex)

    def test_xml_processor_parse_employee_fails_for_invalid_employ_data(self):
        order_processor = XMLOrderProcessor(data=failing_employee_data)
        with pytest.raises(ValidationError) as ex:
            order_processor.parse_employee(data=order_processor.data_dict.get('Employee'))
        assert 'IsAttending' in str(ex)

    def test_xml_processor_parse_order_fails(self):
        order_processor = XMLOrderProcessor(data=failing_order_data)
        with pytest.raises(Exception) as ex:
            order_processor.parse_order(data=order_processor.data_dict.get('Order'))

    def test_xml_processor_parse_order_returns_correct_values(self):
        order_processor = XMLOrderProcessor(data=working_order_data)
        orders = order_processor.parse_order(data=order_processor.data_dict.get('Order'))
        assert len(orders) == 3
        for order in orders:
            assert order.json() == '{"amount": 1, "meal": "Caesar Salad", "id": 42}'
