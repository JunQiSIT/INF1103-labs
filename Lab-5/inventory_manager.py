from pathlib import Path

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

# Generates report of total deliveries processed and number of failed/rejected entries
def display_all():
    return

# Load inventory from file
def load_inventory():
    # Gets the filepath of the current working directory
    filepath = Path(__file__).parent / "inventory.json"
    try:
        filepath.touch(exist_ok=True)
    except Exception as e:
        return f'Exception occured: {e}'

    print('\ninventory.json file found.')
    print('Inventory loaded successfully')

# Save inventory to file for persistence
def save_inventory(current_order_list: list):
    # Gets the filepath of the current working directory
    filepath = Path(__file__).parent / "inventory.json"
    with open(filepath, "a") as f:
        for order in current_order_list:
            f.write(", ".join(order) + "\n")
    print("Order Successfully saved to inventory.json")
    return

def add_product():
    return

def update_stock():
    return

def search_product():
    return

# Main Program
def main():
    print("\n" + "=" * 30)
    print('INVENTORY MANAGEMENT SYSTEM')
    print("=" * 30)
    stored_inventory = load_inventory()

    user_choice = inventory_menu()
    match user_choice:
        case 1:
            print("Display All Products")
        case 2:
            print("Add Product")
        case 3:
            print("Update Stock")
        case 4:
            print("Search Product")
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
