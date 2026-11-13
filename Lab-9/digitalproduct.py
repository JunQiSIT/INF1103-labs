from product import Product

# Classes imports
from supplier import Supplier

# Digital product subclass
class DigitalProduct(Product):
    def __init__(self, product_id: int, product_type: str, name: str, price: float, quantity: int, download_size: float, supplier: Supplier):
        super().__init__(product_id, product_type, name, price, quantity, supplier)
        self._download_size = download_size

    @property
    def download_size(self) -> float:
        return self._download_size
    
    def display_information(self) -> None:
        print(super().display_information() + f" | Download Size: {self.download_size}MB")
        self._supplier.display_information()

    def get_fufilment_info(self) -> None:
        print(f"Digital Product is delivered digitally via download.")
