from pathlib import Path    

# Global Variables
inventory = 0
add_inventory = True
current_orders = []

# Functions
# Retrieves and validates user input for stock quantity
def get_valid_input():
    global add_inventory
    product_name = input("Enter Product Name (or type 'quit' to exit): ")

    if product_name == 'quit':
        return product_name, None, False
    
    quantity_input = input("Enter stock quantity (or type 'quit' to exit): ")

    # Checks if input is quit signal to exit the program
    if quantity_input == 'quit':
        return None, quantity_input, False

    # Checks if the input is a valid integer ignoring the negative sign for validation
    # Afterwards converts user input string to an integer and checks if it is non-negative
    try:
        if not quantity_input.lstrip('-').isdigit():
            print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
            failed_entries += 1
            return product_name, quantity_input, False
        elif int(quantity_input) < 0:
            print("Invalid input. Please enter a non-negative integer.")
            failed_entries += 1
            return product_name, quantity_input, False

    except ValueError: # Exception to catch any unexpected errors during conversion e.g. --3
        print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
        failed_entries += 1
        return product_name, quantity_input, False

    # Return user input if it passes validation
    return product_name, int(quantity_input), True

# Processes the delivery by adding the new value to the current total inventory
def process_delivery(current_order_list: list, order: list):
    if not current_order_list:
        order.insert(0,1)
        current_order_list.append(order)
    else:
        order.insert(0, len(current_order_list) + 1)
        current_order_list.append(order)
    return

# Generates report of total deliveries processed and number of failed/rejected entries
def generate_report(total_units):
    print(f'Total Deliveries Processed: {total_units}')
    return

# Load inventory from file
def load_inventory():
    filepath = Path("./orders.txt")
    try:
        filepath.touch(exist_ok=True)
    except Exception as e:
        return f'Exception occured: {e}'
    return

# Save inventory to file for persistence
def save_inventory():
    return

# Main Program
def main():
    print('Welcome to the Smart Inventory Auditor!')
    # Initialise inventory from file
    load_inventory()
    while True:
        product_input, quantity_input, add_inventory = get_valid_input()

        if quantity_input == 'quit' or product_input == 'quit':
            print("\nExiting Smart Inventory Auditor.")
            generate_report(inventory)
            break

        if add_inventory:
            process_delivery(current_orders, [product_input, quantity_input])

    # Save recorded inventory into file for persistence
    save_inventory()
    
if __name__=="__main__":
    main()
