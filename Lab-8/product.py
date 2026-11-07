from typing import Any
from abc import ABC, abstractmethod

# Classes imports
from supplier import Supplier

# Product class to represent individual products
class Product(ABC):
    # Class initialization
    def __init__(self, product_id: int, product_type: str, name: str, price: float, quantity: int, supplier: Supplier):
        self._product_id = product_id
        self._product_type = product_type
        self._name = name
        self._price = price
        self._quantity = quantity
        self._supplier: Supplier = supplier

    # Properties for product attributes
    # Getters
    @property
    def product_id(self) -> int:
        return self._product_id

    @property
    def product_type(self) -> str:
        return self._product_type
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def quantity(self) -> int:
        return self._quantity

    # Setters
    @quantity.setter
    def quantity(self, new_quantity: int):
        self._quantity = new_quantity

    # Class method
    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> 'Product':
        from physicalproduct import PhysicalProduct
        from digitalproduct import DigitalProduct
        if "_weight" in data:
            return PhysicalProduct(
                product_id=data.get("_product_id"),
                product_type=data.get("_product_type"),
                name=data.get("_name"),
                price=data.get("_price"),
                quantity=data.get("_quantity"),
                weight=data.get("_weight"),
                supplier=Supplier(data.get("_supplier_id"), data.get("_supplier_name"), data.get("_contact_email"))
            )
        
        if "_download_size" in data:
            return DigitalProduct(
                product_id=data.get("_product_id"),
                product_type=data.get("_product_type"),
                name=data.get("_name"),
                price=data.get("_price"),
                quantity=data.get("_quantity"),
                download_size=data.get("_download_size"),
                supplier=Supplier(data.get("_supplier_id"), data.get("_supplier_name"), data.get("_contact_email"))
            )

    # Update stock of existing product
    def update_stock(self, new_quantity: int):
        print("\nProduct found:")
        print("-" * 30)
        print(f"Name: {self._name}")
        print(f"Type: {self._product_type}")
        print(f"Price: ${self._price:.2f}")
        print(f"Current Stock: {self._quantity}")
        print(f"Weight: {getattr(self, '_weight', 'N/A')}kg" if hasattr(self, '_weight') else f"Download Size: {getattr(self, '_download_size', 'N/A')}MB")
        print("-" * 30)
        self._quantity = new_quantity
        print("\nStock updated successfully!")

    def display_information(self):
        return f"ID: {self.product_id} | Type: {self.product_type} | Name: {self.name} | Price: ${self.price:.2f} | Stock: {self.quantity}"

    @abstractmethod
    def get_fufilment_info():
        pass
