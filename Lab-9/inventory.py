from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from product import Product
from supplier import Supplier
from productfactory import ProductFactory

# Inventory class to manage the collection of products
class Inventory:
    # Class initialization
    def __init__(self):
        from oop_inventory_manager import load_inventory
        self._products: list[Product] = load_inventory() or []

    # Add new product to inventory
    def add_product(self, prod_type: str, name: str, price: float, quantity: int, weight: float | None, download_size: float | None, supplier: Supplier) -> None:
        # Create a new Product instance and add it to the running inventory
        prod_id = len(self._products) + 1
        new_product = ProductFactory.create(prod_type, prod_id, name, price, quantity, supplier, weight=weight, download_size=download_size)
        new_product.get_fufilment_info()

        if isinstance(new_product, PhysicalProduct):
            new_product.calculate_shipping_cost()

        self._products.append(new_product)
        print("Product added successfully!")

    # Search for a product by ID
    def search_product(self, target_search_id: int) -> Product | None:
        for product in self._products:
            if product.product_id == target_search_id:
                return product
        return None

    def remove_product(self, product_id: int) -> None:
        product_remove = self.search_product(product_id)
        if product_remove:
            self._products.remove(product_remove)
            print(f"Product ID {product_id} removed successfully.")
        else:
            print(f"Product ID {product_id} not found in the inventory.")
    # Display all inventory items within file
    def display_all(self) -> None:
        if not self._products:
            print("\nNo products found in the inventory.")
            return
        print("\n" + "=" * 30)
        print("Current Inventory")
        print("=" * 30)
        for product in self._products:
            print("-" * 100)
            product.display_information()
            print("-" * 100)
