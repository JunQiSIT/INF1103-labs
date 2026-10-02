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
def display_all():
    try:
        with open(INVENTORY_FILEPATH, "r") as f:
            inventory_data = json.load(f)
            if not inventory_data:
                print("\nNo products found in the inventory.")
                return
            print("\nCurrent Inventory")
            print("-" * 50)
            for product in inventory_data:
                print(f"ID: {product['ID']} | Name: {product['Name']} | Price: ${product['Price']:.2f} | Stock: {product['Quantity']}")
            print("-" * 50)
    except FileNotFoundError:
        print("\nInventory file not found. Please ensure the inventory.json file exists.")
    except json.JSONDecodeError:
        print("\nError decoding JSON from the inventory file. Please check the file format.")
    return

# Load inventory from file
def load_inventory():
    # Gets the filepath of the current working directory
    try:
        INVENTORY_FILEPATH.touch(exist_ok=True)
    except Exception as e:
        return f'Exception occured: {e}'

    print('\ninventory.json file found.')
    print('Inventory loaded successfully')

# Save inventory to file for persistence
def save_inventory(current_order_list: list):
    # Gets the filepath of the current working directory
    with open(INVENTORY_FILEPATH, "a") as f:
        for order in current_order_list:
            f.write(", ".join(order) + "\n")
    print("Order Successfully saved to inventory.json")
    return

def add_product():
    print("\nAdd New Product")
    with open(INVENTORY_FILEPATH, "r") as f:
        inventory_data = json.load(f)

    new_product = {
        "ID": len(inventory_data) + 1,
        "Name": input("Enter product name: "),
        "Price": float(input("Enter product price: ")),
        "Quantity": int(input("Enter product quantity: "))
    }
    inventory_data.append(new_product)
    with open(INVENTORY_FILEPATH, "w") as f:
        json.dump(inventory_data, f, indent=4)
    print("Product added successfully!")
    return

def update_stock():
    print("\nUpdate Stock")
    with open(INVENTORY_FILEPATH, "r") as f:
        inventory_data = json.load(f)
    product_id = int(input("Enter Product ID: "))
    for product in inventory_data:
        if product["ID"] == product_id:
            print("\nProduct found:")
            print(f'Name: {product['Name']}')
            print(f'Current Stock: {product['Quantity']}')
            new_quantity = int(input("\nNew Stock Quantity: "))
            product["Quantity"] = new_quantity
            with open(INVENTORY_FILEPATH, "w") as f:
                json.dump(inventory_data, f, indent=4)
            print("\nStock updated successfully!")
            return
    print("Product not found.")
    return

def search_product():
    print("\nSearch Product")
    with open(INVENTORY_FILEPATH, "r") as f:
        inventory_data = json.load(f)
    search_id = int(input("Enter Product ID: "))
    for product in inventory_data:
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
                display_all()
            case 2:
                add_product()
            case 3:
                update_stock()
            case 4:
                search_product()
            case 5:
                print("Save Inventory")
            case 6:
                print("\nSaving inventory before exit...")
                # Save inventory to file for persistence

                print("\nThank you for using the Inventory Management System. Goodbye!")
                print("Program Terminated.")
                return
    

if __name__=="__main__":
    main()
