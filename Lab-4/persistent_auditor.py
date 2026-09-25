from pathlib import Path    

# Global Variables
inventory = 0
add_inventory = True

# Functions
# Retrieves and validates user input for stock quantity
def get_valid_input():
    global add_inventory
    product_name = input("Enter Product Name (or type 'quit' to exit): ")

    if product_name == 'quit':
        return product_name, None, False
    
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")

    # Checks if input is quit signal to exit the program
    if user_input == 'quit':
        return None, user_input, False

    # Checks if the input is a valid integer ignoring the negative sign for validation
    # Afterwards converts user input string to an integer and checks if it is non-negative
    try:
        if not user_input.lstrip('-').isdigit():
            print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
            failed_entries += 1
            return product_name, user_input, False
        elif int(user_input) < 0:
            print("Invalid input. Please enter a non-negative integer.")
            failed_entries += 1
            return product_name, user_input, False

    except ValueError: # Exception to catch any unexpected errors during conversion e.g. --3
        print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
        failed_entries += 1
        return product_name, user_input, False

    # Return user input if it passes validation
    return product_name, int(user_input), True

# Processes the delivery by adding the new value to the current total inventory
def process_delivery(current_total, new_value):
    return current_total + new_value

# Generates report of total deliveries processed and number of failed/rejected entries
def generate_report(total_units):
    print(f'Total Deliveries Processed: {total_units}')
    return

# Load inventory from file
def load_inventory():
    filepath = Path("./orders.txt")
    filepath.touch(exist_ok=True)
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
        product_input, user_input, add_inventory = get_valid_input()

        if user_input == 'quit' or product_input == 'quit':
            print("\nExiting Smart Inventory Auditor.")
            generate_report(inventory)
            break

        if add_inventory:
            return

    # Save recorded inventory into file for persistence
    save_inventory()
    
if __name__=="__main__":
    main()
