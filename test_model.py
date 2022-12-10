from datetime import date, timedelta
import pytest

from model import Batch, OrderLine

# from model import ...

today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)


def test_allocating_to_a_batch_reduces_the_available_quantity():
    init_quantity = 20
    order_line_quantity = 2
    batch = Batch(1, "SMALL-TABLE", init_quantity)
    order_line = OrderLine("SMALL-TABLE", order_line_quantity)
    batch.allocate(order_line)
    assert batch.quantity == init_quantity - order_line_quantity


def test_can_allocate_if_available_greater_than_required():
    init_quantity = 20
    order_line_quantity = 2
    batch = Batch(1, "SMALL-TABLE", init_quantity)
    order_line = OrderLine("SMALL-TABLE", order_line_quantity)
    batch.allocate(order_line)


def test_cannot_allocate_if_available_smaller_than_required():
    init_quantity = 20
    order_line_quantity = 22
    batch = Batch(1, "SMALL-TABLE", init_quantity)
    order_line = OrderLine("SMALL-TABLE", order_line_quantity)
    with pytest.raises(Exception):
        batch.allocate(order_line)


def test_can_allocate_if_available_equal_to_required():
    init_quantity = 20
    order_line_quantity = 20
    batch = Batch(1, "SMALL-TABLE", init_quantity)
    order_line = OrderLine("SMALL-TABLE", order_line_quantity)
    batch.allocate(order_line)


def test_prefers_warehouse_batches_to_shipments():
    pytest.fail("todo")


def test_prefers_earlier_batches():
    pytest.fail("todo")
