from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class OrderLine:
    sku: str
    quantity: int


@dataclass
class Order:
    reference: int
    order_lines: List[OrderLine]


class Batch:
    reference_number: int
    sku: str
    quantity: int

    def __init__(self, 
                 reference_number: int,
                 sku: str,
                 quantity: int) -> None:
        self.reference_number = reference_number
        self.sku = sku
        self.quantity = quantity
    
    def allocate(self, order_line: OrderLine) -> None:
        if self.quantity >= order_line.quantity:
            self.quantity -= order_line.quantity
        else:
            raise ValueError("Available quantity in batch is less than OrderLine quatity")
        
