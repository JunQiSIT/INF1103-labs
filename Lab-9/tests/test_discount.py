import inspect
import pytest

from bulkdiscount import BulkDiscount
from discountstrategy import DiscountStrategy
from nodiscount import NoDiscount
from order import Order
from percentagediscount import PercentageDiscount
from physicalproduct import PhysicalProduct
from studentdiscount import StudentDiscount
from supplier import Supplier


@pytest.fixture
def sample_order() -> Order:
    supplier = Supplier(1, "Acme Corp", "sales@acme.com")
    product = PhysicalProduct(1, "physical", "Monitor", 125.0, 10, 3.5, supplier)
    order = Order("ORD-001")
    order.add_order_line(product, 2)  # Subtotal = 250.0
    return order


def test_order_default_no_discount(sample_order: Order) -> None:
    assert sample_order.calculate_total() == pytest.approx(250.0)


def test_order_percentage_discount(sample_order: Order) -> None:
    sample_order.set_discount(PercentageDiscount(10))
    assert sample_order.calculate_total() == pytest.approx(225.0)


def test_order_bulk_discount_applied_and_not_applied(sample_order: Order) -> None:
    sample_order.set_discount(BulkDiscount(200, 20))
    assert sample_order.calculate_total() == pytest.approx(230.0)

    # Order below threshold should remain unchanged
    supplier = Supplier(1, "Acme Corp", "sales@acme.com")
    cheap_item = PhysicalProduct(2, "physical", "Mouse", 50.0, 10, 0.2, supplier)
    small_order = Order("ORD-002", BulkDiscount(200, 20))
    small_order.add_order_line(cheap_item, 1)
    assert small_order.calculate_total() == pytest.approx(50.0)


def test_order_student_discount_and_swapping_strategies(sample_order: Order) -> None:
    sample_order.set_discount(BulkDiscount(200, 20))
    assert sample_order.calculate_total() == pytest.approx(230.0)

    # Swap strategy on existing order using set_discount()
    sample_order.set_discount(StudentDiscount(15))
    assert sample_order.calculate_total() == pytest.approx(212.5)


def test_new_discount_strategy_works_without_modifying_order(sample_order: Order) -> None:
    class VIPFlatDiscount(DiscountStrategy):
        def apply(self, total: float) -> float:
            return max(0.0, total - 50.0)

    sample_order.set_discount(VIPFlatDiscount())
    assert sample_order.calculate_total() == pytest.approx(200.0)


def test_order_contains_no_discount_if_elif_logic() -> None:
    source = inspect.getsource(Order)
    assert "if " not in source and "elif " not in source
    assert "PercentageDiscount" not in source
    assert "BulkDiscount" not in source
