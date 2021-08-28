from abc import ABC, abstractmethod
from typing import List, Dict, Union
from momox.order_processor.dto import ProcessorEmployeeDto, ProcessorOrderItemDto


class OrderProcessor(ABC):
    @abstractmethod
    def get_employees(self) -> List[ProcessorEmployeeDto]:
        """returns an List of employee data"""

    @abstractmethod
    def parse_employee(self, *, data: Dict[str, Union[str, Dict[str, str]]]) -> ProcessorEmployeeDto:
        """returns an employee data"""

    @classmethod
    def parse_order(cls, *, data: str) -> List[ProcessorOrderItemDto]:
        """returns an List of employee orders data"""
