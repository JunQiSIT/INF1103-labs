from product import Product

# Digital product subclass
class DigitalProduct(Product):
    def __init__(self, product_id: int, product_type: str, name: str, price: float, quantity: int, download_size: float):
        super().__init__(product_id, product_type, name, price, quantity)
        self._download_size = download_size

    @property
    def download_size(self) -> float:
        return self._download_size
    
    def display_information(self):
        print(super().display_information() + f" | Download Size: {self.download_size}MB")

    def get_fufilment_info(self):
        print(f"Digital Product is delivered digitally via download.")
