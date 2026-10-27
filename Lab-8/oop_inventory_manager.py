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
                deserialize_products = [Product(**product) for product in inventory_data]
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
        save = [product.__dict__ for product in running_inventory_data]
        json.dump(save, f, indent=4)
    print("Inventory saved Successfully to inventory.json")
    return

# Classes
# Product class to represent individual products
class Product:
    def __init__(self, product_id: int, name: str, price: float, quantity: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

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

    # Update stock of existing product
    def update_stock(self, product_id: int, new_quantity: int):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = new_quantity
                return True
        return False

    # Search for a product by ID
    def search_product(self, product_id: int) -> Any:
        for product in self.products:
            if product.product_id == product_id:
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
                inventory.update_stock()
            case 4:
                inventory.search_product()
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
