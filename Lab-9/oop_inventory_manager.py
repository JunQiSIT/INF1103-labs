from pathlib import Path
import json

# Constants
INVENTORY_FILEPATH = Path(__file__).parent / "inventory.json"

# Classes
from product import Product
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from inventory import Inventory
from supplier import Supplier
from order import Order
from nodiscount import NoDiscount
from percentagediscount import PercentageDiscount
from bulkdiscount import BulkDiscount
from studentdiscount import StudentDiscount

# Functions
# Menu for user to select
def inventory_menu():
    while True:
        print("\n--------MENU--------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Remove Product")
        print("5. Order Product")
        print("6. Search Product")
        print("7. Save Inventory")
        print("8. Exit")
        print("--------------------")

        user_input = input("Enter your choice (1-8): ")
        if not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 8:
            print("\nInvalid choice. Please select a number between 1 and 8.")
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
    save_data = []

    for product in running_inventory_data:
        # Shallow copy product internal dictionary
        prod_dict = product.__dict__.copy()

        # Remove the nested _supplier object reference
        supplier_obj = prod_dict.pop("_supplier", None)

        # Flatten supplier attributes to top-level keys
        if supplier_obj:
            prod_dict["_supplier_id"] = supplier_obj.supplier_id
            prod_dict["_supplier_name"] = supplier_obj.supplier_name
            prod_dict["_contact_email"] = supplier_obj.contact_email
        else:
            prod_dict["_supplier_id"] = None
            prod_dict["_supplier_name"] = None
            prod_dict["_contact_email"] = None

        save_data.append(prod_dict)
    
    # Serialize products to dictionaries before saving
    with open(INVENTORY_FILEPATH, "w") as f: 
        json.dump(save_data, f, indent=4)
    print("Inventory saved Successfully to inventory.json")
    return

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
                while True:
                    product_type = input("Enter product type (physical/digital): ").strip().lower()
                    if product_type in ["physical", "digital"]:
                        break
                    else:
                        print("Invalid product type. Please enter 'physical' or 'digital'.")
                name = input("Enter product name: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                supplier_name = input("Enter supplier name: ")
                supplier_email = input("Enter supplier contact email: ")
                supplier = Supplier(len(inventory._products) + 1, supplier_name, supplier_email)

                if product_type == "physical":
                    weight = float(input("Enter product weight (kg): "))
                    inventory.add_product(product_type, name, price, quantity, weight, None, supplier)
                else:
                    download_size = float(input("Enter digital file size (MB): "))
                    inventory.add_product(product_type, name, price, quantity, None, download_size, supplier)
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
                print("\nRemove Product")
                product_id = int(input("Enter Product ID to remove: "))
                inventory.remove_product(product_id)
            case 5:
                print("\nOrder Product")
                order_id_list = []
                order_id = input("Enter Order ID: ")
                while True:
                    prod_id = input("Enter Product ID of product to order (q to quit): ")
                    if prod_id == 'q':
                        break
                    else:
                        order_id_list.append(prod_id)

                order = Order(order_id)
                for prod_id in order_id_list:
                    order_product = inventory.search_product(int(prod_id))
                    if order_product:
                        order.add_order_line(order_product, order_product.quantity)
                    else:
                        print(f"\nProduct of product ID {prod_id} not found.")

                # Select and apply DiscountStrategy
                print("\nSelect Discount Strategy:")
                print("1. Percentage Discount")
                print("2. Bulk Discount")
                print("3. Student Discount")
                print("No selection, default: No Discount")
                discount_choice = input("Enter choice (1-3): ").strip()

                if discount_choice == "1":
                    percentage = float(input("Enter discount percentage (e.g., 10 for 10%): "))
                    order.set_discount(PercentageDiscount(percentage))
                elif discount_choice == "2":
                    threshold = float(input("Enter minimum order threshold (e.g., 200): "))
                    amount = float(input("Enter discount amount (e.g., 20): "))
                    order.set_discount(BulkDiscount(threshold, amount))
                elif discount_choice == "3":
                    student_discount_rate = float(input("Enter student discount rate (e.g., 15 for 15%): "))
                    order.set_discount(StudentDiscount(student_discount_rate))
                else:
                    order.set_discount(NoDiscount())

                total_cost = order.calculate_total()
                print(f"Total cost of the order: ${total_cost:.2f}")
                    
            case 6:
                print("\nSearch Product")
                search_id = int(input("Enter Product ID: "))
                found = inventory.search_product(search_id)

                if found:
                    print("\nProduct found:")
                    print("-" * 30)
                    print("Product info")
                    print(f"ID: {found.product_id}")
                    print(f"Type: {found.product_type}")
                    print(f"Name: {found.name}")
                    print(f"Price: ${found.price:.2f}")
                    print(f"Stock: {found.quantity}")
                    if isinstance(found, PhysicalProduct):
                        print(f"Weight: {found.weight}kg")
                    elif isinstance(found, DigitalProduct):
                        print(f"Download Size: {found.download_size}MB")
                    print("\nSupplier info")
                    print(f"Supplier ID: {found._supplier._supplier_id}")
                    print(f"Supplier Name: {found._supplier._supplier_name}")
                    print(f"Contact Email: {found._supplier._contact_email}")
                    print("-" * 30)
                else:
                    print("\nProduct not found.")
            case 7:
                save_inventory(inventory._products)
            case 8:
                print("\nSaving inventory before exit...")
                
                # Save inventory to file for persistence
                save_inventory(inventory._products)
                print("\nThank you for using the Inventory Management System. Goodbye!")
                print("Program Terminated.")
                return

if __name__=="__main__":
    main()
