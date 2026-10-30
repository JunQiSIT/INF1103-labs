from pathlib import Path
from typing import Any
import json

# Constants
INVENTORY_FILEPATH = Path(__file__).parent / "inventory.json"

# Functions
# Menu for user to select
def inventory_menu():
    while True:
        print("\n--------MENU--------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("--------------------")

        user_input = input("Enter your choice (1-6): ")
        if not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 6:
            print("\nInvalid choice. Please select a number between 1 and 6.")
            continue
        else:
            return int(user_input)

# Load inventory from file
def load_inventory():
    # Creates the inventory.json file if it does not exist
    try:
        INVENTORY_FILEPATH.touch(exist_ok=True)
    except Exception as e:
        return f'Exception occured: {e}'

    # Tries to open and load inventory data from the inventory.json file
    try:
        with open(INVENTORY_FILEPATH, "r") as f:
            inventory_data = json.load(f)
            if not inventory_data:
                return None
            else:
                # Deserialize the loaded inventory data into Product instances
                deserialize_products = [Product.from_dict(product) for product in inventory_data]
                print('\ninventory.json file found.')
                print('Inventory loaded successfully')
                return deserialize_products
    except FileNotFoundError:
        print("\nInventory file not found. Please ensure the inventory.json file exists.")
    except json.JSONDecodeError:
        print("\nError decoding JSON from the inventory file. Please check the file format.")

# Save inventory to file for persistence
def save_inventory(running_inventory_data):
    print("\nSaving inventory...")
    with open(INVENTORY_FILEPATH, "w") as f:
        # Serialize products to a list of dictionaries before saving
        save = [product.__dict__ for product in running_inventory_data]
        json.dump(save, f, indent=4)
    print("Inventory saved Successfully to inventory.json")
    return

# Classes
# Product class to represent individual products
class Product:
    # Class initialization
    def __init__(self, product_id: int, name: str, price: float, quantity: int):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity = quantity

    # Properties for product attributes
    # Getters
    @property
    def product_id(self) -> int:
        return self._product_id

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
        return cls(
            product_id=data.get("_product_id"),
            name=data.get("_name"),
            price=data.get("_price"),
            quantity=data.get("_quantity")
        )

    # Update stock of existing product
    def update_stock(self, new_quantity: int):
        print("\nProduct found:")
        print(f"Name: {self._name}")
        print(f"Price: ${self._price:.2f}")
        print(f"Current Stock: {self._quantity}")
        self._quantity = new_quantity
        print("\nStock updated successfully!")
        

# Inventory class to manage the collection of products
class Inventory:
    # Class initialization
    def __init__(self):
        self.products = load_inventory() or []

    # Add new product to inventory
    def add_product(self, name: str, price: float, quantity: int):
        # Create a new Product instance and add it to the running inventory
        prod_id = len(self.products) + 1
        new_product = Product(prod_id, name, price, quantity)
        self.products.append(new_product)
        print("Product added successfully!")

    # Search for a product by ID
    def search_product(self, target_search_id: int) -> Product | None:
        for product in self.products:
            if product.product_id == target_search_id:
                return product
        return None

    # Display all inventory items within file
    def display_all(self):
        if not self.products:
            print("\nNo products found in the inventory.")
            return
        print("\nCurrent Inventory")
        print("-" * 50)
        for product in self.products:
            print(f"ID: {product.product_id} | Name: {product.name} | Price: ${product.price:.2f} | Stock: {product.quantity}")
        print("-" * 50)

# Main Program
def main():
    print("\n" + "=" * 30)
    print('INVENTORY MANAGEMENT SYSTEM')
    print("=" * 30)
    inventory = Inventory()

    while True:
        user_choice = inventory_menu()
        match user_choice:
            case 1:
                inventory.display_all()
            case 2:
                print("\nAdd New Product")
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                inventory.add_product(name, price, quantity)
            case 3:
                print("\nUpdate Stock")
                product_id = int(input("Enter Product ID: "))
                found_product = inventory.search_product(product_id)
                if found_product:
                    new_quantity = int(input("New Stock Quantity: "))
                    found_product.update_stock(new_quantity)
                else:
                    print("\nProduct not found.")
            case 4:
                print("\nSearch Product")
                search_id = int(input("Enter Product ID: "))
                found = inventory.search_product(search_id)

                if found:
                    print("\nProduct found:")
                    print("-" * 30)
                    print(f"ID: {found.product_id}")
                    print(f"Name: {found.name}")
                    print(f"Price: ${found.price:.2f}")
                    print(f"Stock: {found.quantity}")
                    print("-" * 30)
                else:
                    print("\nProduct not found.")
            case 5:
                save_inventory(inventory.products)
            case 6:
                print("\nSaving inventory before exit...")
                
                # Save inventory to file for persistence
                save_inventory(inventory.products)
                print("\nThank you for using the Inventory Management System. Goodbye!")
                print("Program Terminated.")
                return

if __name__=="__main__":
    main()
