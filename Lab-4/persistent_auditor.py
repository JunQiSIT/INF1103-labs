from pathlib import Path

# Functions
# Retrieves and validates user input for stock quantity
def get_valid_input(failed_entries):
    product_input = input("\nEnter Product Name (or type 'quit' to exit): ")

    if product_input == 'quit':
        return product_input, None, False, failed_entries
    
    quantity_input = input("Enter stock quantity (or type 'quit' to exit): ")

    # Checks if input is quit signal to exit the program
    if quantity_input == 'quit':
        return None, quantity_input, False, failed_entries

    # Checks if the input is a valid integer ignoring the negative sign for validation
    # Afterwards converts user input string to an integer and checks if it is non-negative
    try:
        if not quantity_input.lstrip('-').isdigit():
            print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
            failed_entries += 1
            return product_input, quantity_input, False, failed_entries
        elif int(quantity_input) < 0:
            print("Invalid input. Please enter a non-negative integer.")
            failed_entries += 1
            return product_input, quantity_input, False, failed_entries

    except ValueError: # Exception to catch any unexpected errors during conversion e.g. --3
        print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
        failed_entries += 1
        return product_input, quantity_input, False, failed_entries

    # Return user input if it passes validation
    return product_input, int(quantity_input), True, failed_entries

# Processes the delivery by adding the new value to the current total inventory
def process_delivery(current_total, new_value, current_order_list: list, order: list, existing_count):
    running_inventory = current_total + new_value
    # If inventory.txt contains previous orders start count from last order
    if existing_count:
        order.insert(0, str(existing_count + 1))
        current_order_list.append(order)
    # If list is empty append start index
    elif not current_order_list:
        order.insert(0,'1001')
        current_order_list.append(order)
    else:
        order.insert(0, str(int(current_order_list[-1][0]) + 1))
        current_order_list.append(order)
    return running_inventory, ", ".join(order), current_order_list, None

# Calculates 10% tax on the delivery amount
def calculate_tax(amount):
    return amount * 0.1

# Generates report of total deliveries processed and number of failed/rejected entries
def generate_report(total_units,failed_attempts):
    print("\n========Audit Report========")
    print(f'Total Deliveries Processed: {total_units}')
    print(f'Number of Failed/Rejected Entries: {failed_attempts}')
    return

# Load inventory from file
def load_inventory():
    filepath = Path(__file__).parent / "inventory.txt"
    try:
        filepath.touch(exist_ok=True)
    except Exception as e:
        return f'Exception occured: {e}'

    with open(filepath, 'r') as f:
        content = f.read()
    print("Currrent Orders:")
    if not content:
        print("  (No previous orders found)")
        print("-" * 30)
        return 0
    else:
        print(content)
        return int(content.splitlines()[-1].split(',')[0])

# Save inventory to file for persistence
def save_inventory(current_order_list: list):
    filepath = Path(__file__).parent / "inventory.txt"
    with open(filepath, "a") as f:
        for order in current_order_list:
            f.write(", ".join(order) + "\n")
    print("Order Successfully saved to inventory.txt")
    return

# Main Program
def main():
    print('Welcome to the Smart Inventory Auditor!')
    prev_count = load_inventory()
    # Variables
    inventory = 0
    current_orders = []
    failed_entries = 0
    add_inventory = True
    while True:
        product_input, quantity_input, add_inventory, failed_entries = get_valid_input(failed_entries)

        if quantity_input == 'quit' or product_input == 'quit':
            print("\nExiting Smart Inventory Auditor.")
            save_inventory(current_orders)
            generate_report(inventory, failed_entries)
            break

        if add_inventory:
            inventory, order, current_orders, prev_count = process_delivery(inventory, quantity_input, current_orders, [product_input, str(quantity_input)], prev_count)
            tax = calculate_tax(quantity_input)
            print(f'\nNew Order Added: {order}')
            print(f'Tax: ${tax:.2f} | Total Inventory: {inventory}')

if __name__=="__main__":
    main()
