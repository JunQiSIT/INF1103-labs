# Global Variables
inventory = 0
failed_entries = 0

# Functions
def get_valid_input():
    global failed_entries
    global add_inventory
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")

    # Checks if input is quit signal to exit the program
    if user_input == 'quit':
        return user_input, False, failed_entries

    # Checks if the input is a valid integer ignoring the negative sign for validation
    # Afterwards converts user input string to an integer and checks if it is non-negative
    try:
        if not user_input.lstrip('-').isdigit():
            print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
            failed_entries += 1
            return user_input, False, failed_entries
        elif int(user_input) < 0:
            print("Invalid input. Please enter a non-negative integer.")
            failed_entries += 1
            return user_input, False, failed_entries

    except ValueError: # Exception to catch any unexpected errors during conversion e.g. --3
        print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
        failed_entries += 1
        return user_input, False, failed_entries

    # Return user input if it passes validation
    return int(user_input), True, failed_entries

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return

def generate_report(total_units,failed_attempts):
    return

# Main Program
print('Welcome to the Smart Inventory Auditor!')
while True:
    add_inventory = True
    user_input, add_inventory, failed_entries = get_valid_input()

    if user_input == 'quit':
        print("Exiting Smart Inventory Auditor.")
        break

    if add_inventory:
        inventory = process_delivery(inventory, user_input)

