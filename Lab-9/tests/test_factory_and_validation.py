import inspect
import pytest

from digitalproduct import DigitalProduct
from inventory import Inventory
from order import Order
from orderline import OrderLine
from physicalproduct import PhysicalProduct
from productfactory import ProductFactory
from supplier import Supplier


@pytest.fixture
def supplier() -> Supplier:
    return Supplier(1, "TechSupply", "info@techsupply.com")


def test_factory_creates_physical_and_digital_products(supplier: Supplier) -> None:
    phys = ProductFactory.create("physical", 1, "Desk Lamp", 25.0, 10, supplier, weight=1.2)
    digi = ProductFactory.create("digital", 2, "Photo Editor", 49.90, 100, supplier, download_size=500.0)

    assert isinstance(phys, PhysicalProduct)
    assert isinstance(digi, DigitalProduct)


def test_factory_unknown_product_type_raises_value_error(supplier: Supplier) -> None:
    with pytest.raises(ValueError, match="Unknown product type: service"):
        ProductFactory.create("service", 3, "Installation", 30.0, 5, supplier)


def test_inventory_uses_product_factory_instead_of_direct_instantiation() -> None:
    add_source = inspect.getsource(Inventory.add_product)
    assert "ProductFactory.create" in add_source
    assert "PhysicalProduct(" not in add_source
    assert "DigitalProduct(" not in add_source


@pytest.mark.parametrize("invalid_price", [0, -0.01, -100.0])
def test_product_rejects_non_positive_price(supplier: Supplier, invalid_price: float) -> None:
    with pytest.raises(ValueError, match="greater than zero"):
        ProductFactory.create("physical", 1, "Bad Price Item", invalid_price, 5, supplier, weight=1.0)


def test_product_rejects_negative_stock_on_init_and_update(supplier: Supplier) -> None:
    with pytest.raises(ValueError, match="cannot be negative"):
        ProductFactory.create("digital", 1, "E-Book", 15.0, -1, supplier, download_size=10.0)

    valid_product = ProductFactory.create("digital", 1, "E-Book", 15.0, 5, supplier, download_size=10.0)
    with pytest.raises(ValueError, match="cannot be negative"):
        valid_product.update_stock(-3)


@pytest.mark.parametrize("invalid_qty", [0, -1, -10])
def test_order_line_rejects_non_positive_quantity(supplier: Supplier, invalid_qty: int) -> None:
    product = ProductFactory.create("physical", 1, "Keyboard", 80.0, 10, supplier, weight=0.8)

    with pytest.raises(ValueError, match="greater than zero"):
        OrderLine(product, invalid_qty)

    order = Order("ORD-100")
    with pytest.raises(ValueError, match="greater than zero"):
        order.add_order_line(product, invalid_qty)
