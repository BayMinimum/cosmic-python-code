from typing import List


class OrderLine:
    sku: str
    quantity: int


class Order:
    reference: int
    order_lines: List[OrderLine]


class Batch:
    reference_number: int
    sku: str
    quantity: int
