from canbeshipped import CanBeShipped
from product import Product

# Classes imports
from supplier import Supplier

# Physical product subclass
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: int, product_type: str, name: str, price: float, quantity: int, weight: float, supplier: Supplier):
        super().__init__(product_id, product_type, name, price, quantity, supplier)
        self._weight = weight

    @property
    def weight(self) -> float:
        return self._weight

    def display_information(self):
        print(super().display_information() + f" | Weight: {self.weight}kg")
        self._supplier.display_information()

    def get_fufilment_info(self):
        print(f"Physical Product requires physical shipping.")

    def calculate_shipping_cost(self):
        # shipping cost: $5 per kg
        print(f"Shipping cost for {self._name}: ${self._weight * 5.0:.2f}")
