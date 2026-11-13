from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from product import Product
from supplier import Supplier

class ProductFactory:
    @staticmethod
    def create(product_type, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier) -> Product:
        if product_type == "physical":
            return PhysicalProduct(product_id, name, price, stock_quantity, supplier)
        elif product_type == "digital":
            return DigitalProduct(product_id, name, price, stock_quantity, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")