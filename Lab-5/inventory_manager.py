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

# Display all inventory items within file
def display_all(running_inventory_data):
    if not running_inventory_data:
        print("\nNo products found in the inventory.")
        return
    print("\nCurrent Inventory")
    print("-" * 50)
    for product in running_inventory_data:
        print(f"ID: {product['ID']} | Name: {product['Name']} | Price: ${product['Price']:.2f} | Stock: {product['Quantity']}")
    print("-" * 50)
    return

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
                print('\ninventory.json file found.')
                print('Inventory loaded successfully')
                return inventory_data
    except FileNotFoundError:
        print("\nInventory file not found. Please ensure the inventory.json file exists.")
    except json.JSONDecodeError:
        print("\nError decoding JSON from the inventory file. Please check the file format.")

# Save inventory to file for persistence
def save_inventory(running_inventory_data):
    print("\nSaving inventory...")
    with open(INVENTORY_FILEPATH, "w") as f:
        json.dump(running_inventory_data, f, indent=4)
    print("Inventory saved Successfully to inventory.json")
    return

# Add new product to inventory
def add_product(running_inventory_data):
    print("\nAdd New Product")
    new_product = {
        "ID": len(running_inventory_data) + 1,
        "Name": input("Enter product name: "),
        "Price": float(input("Enter product price: ")),
        "Quantity": int(input("Enter product quantity: "))
    }
    running_inventory_data.append(new_product)
    print("Product added successfully!")
    return running_inventory_data

# Update stock of existing product
def update_stock(running_inventory_data):
    print("\nUpdate Stock")
    product_id = int(input("Enter Product ID: "))
    for product in running_inventory_data:
        if product["ID"] == product_id:
            print("\nProduct found:")
            print(f'Name: {product['Name']}')
            print(f'Current Stock: {product['Quantity']}')
            new_quantity = int(input("\nNew Stock Quantity: "))
            product["Quantity"] = new_quantity
            print("\nStock updated successfully!")
            return running_inventory_data
    print("Product not found.")
    return running_inventory_data

# Search for a product by ID
def search_product(running_inventory_data):
    print("\nSearch Product")
    search_id = int(input("Enter Product ID: "))
    for product in running_inventory_data:
        if product["ID"] == search_id:
            print("\nProduct found:")
            print("-" * 30)
            print(f'ID: {product['ID']}')
            print(f'Name: {product['Name']}')
            print(f'Price: ${product['Price']:.2f}')
            print(f'Stock: {product['Quantity']}')
            print("-" * 30)
            return
    print("\nProduct not found.")
    return

# Main Program
def main():
    print("\n" + "=" * 30)
    print('INVENTORY MANAGEMENT SYSTEM')
    print("=" * 30)
    stored_inventory = load_inventory()

    while True:
        user_choice = inventory_menu()
        match user_choice:
            case 1:
                display_all(stored_inventory)
            case 2:
                stored_inventory = add_product(stored_inventory)
            case 3:
                stored_inventory = update_stock(stored_inventory)
            case 4:
                search_product(stored_inventory)
            case 5:
                save_inventory(stored_inventory)
            case 6:
                print("\nSaving inventory before exit...")
                
                # Save inventory to file for persistence
                save_inventory(stored_inventory)
                print("\nThank you for using the Inventory Management System. Goodbye!")
                print("Program Terminated.")
                return

if __name__=="__main__":
    main()
