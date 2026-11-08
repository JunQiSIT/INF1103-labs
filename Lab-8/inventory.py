from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from product import Product
from supplier import Supplier

# Inventory class to manage the collection of products
class Inventory:
    # Class initialization
    def __init__(self):
        from oop_inventory_manager import load_inventory
        self._products: list[Product] = load_inventory() or []

    # Add new product to inventory
    def add_product(self, prod_type: str, name: str, price: float, quantity: int, weight: float | None, download_size: float | None, supplier: Supplier):
        # Create a new Product instance and add it to the running inventory
        prod_id = len(self._products) + 1
        if prod_type == "physical":
            new_product = PhysicalProduct(prod_id, prod_type, name, price, quantity, weight, supplier)
            new_product.get_fufilment_info()
            new_product.calculate_shipping_cost()
        else:
            new_product = DigitalProduct(prod_id, prod_type, name, price, quantity, download_size, supplier)
            new_product.get_fufilment_info()
        self._products.append(new_product)
        print("Product added successfully!")

    # Search for a product by ID
    def search_product(self, target_search_id: int) -> Product | None:
        for product in self._products:
            if product.product_id == target_search_id:
                return product
        return None

    # Display all inventory items within file
    def display_all(self):
        if not self._products:
            print("\nNo products found in the inventory.")
            return
        print("\n" + "=" * 30)
        print("Current Inventory")
        print("=" * 30)
        for product in self._products:
            print("-" * 100)
            if isinstance(product, PhysicalProduct):
                product.display_information()
            elif isinstance(product, DigitalProduct):
                product.display_information()
            print("-" * 100)
