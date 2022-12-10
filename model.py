from dataclasses import dataclass
from datetime import date, datetime
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
                 quantity: int,
                 eta: Optional[date] = None) -> None:
        self.reference_number = reference_number
        self.sku = sku
        self.quantity = quantity
        self.eta = eta
    
    def allocate(self, order_line: OrderLine) -> None:
        if self.quantity >= order_line.quantity:
            self.quantity -= order_line.quantity
        else:
            raise ValueError("Available quantity in batch is less than OrderLine quatity")
        

def allocate(batches: List[Batch], order_line: OrderLine) -> None:
    batches_sorted_by_eta = sorted(batches, key=lambda batch: batch.eta or datetime.fromtimestamp(0).date())
    for batch in batches_sorted_by_eta:
        try: 
            batch.allocate(order_line)
            return
        except ValueError:
            continue
    raise ValueError("No batch could be allocated for given OrderLine")
