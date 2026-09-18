# Global Variables
inventory = 0
failed_entries = 0

# Functions
def get_valid_input():
    global failed_entries
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")

    # Checks if input is quit signal to exit the program
    if user_input == 'quit':
        return user_input, False, failed_entries

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

    return user_input, True, failed_entries

def process_delivery(current_total, new_value):
    return

def calculate_tax(amount):
    return

def generate_report(total_units,failed_attempts):
    return

# Main Program
print('Welcome to the Smart Inventory Auditor!')
while True:
    add_inventory = True
    user_input, add_inventory, failed_entries = get_valid_input()
    print(user_input)
    print(add_inventory)
    print(failed_entries)
