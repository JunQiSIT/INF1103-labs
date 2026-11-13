from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from product import Product
from supplier import Supplier

class ProductFactory:
    @staticmethod
    def create(product_type, product_id: str, name: str, price: float, stock_quantity: int, supplier: Supplier, weight: float | None = None, download_size: float | None = None) -> Product:
        if product_type == "physical":
            weight = weight if weight is not None else 0.0
            return PhysicalProduct(product_id, product_type, name, price, stock_quantity, weight, supplier)
        elif product_type == "digital":
            download_size = download_size if download_size is not None else 0.0
            return DigitalProduct(product_id, product_type, name, price, stock_quantity,  download_size, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")