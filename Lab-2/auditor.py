inventory = 0
failed_entries = 0


print('Welcome to the Smart Inventory Auditor!')
while True:
    add_inventory = True
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")

    if user_input == 'quit':
        print("Exiting Smart Inventory Auditor.")
        print(f'Total Units Processed: {inventory}')
        print(f'Number of Failed/Rejected entries: {failed_entries}')
        break    

    # Checks if the input is a valid integer ignoring the negative sign for validation
    # Afterwards converts user input string to an integer and checks if it is non-negative
    try:
        if not user_input.lstrip('-').isdigit():
            print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
            failed_entries += 1
            add_inventory = False
        elif int(user_input) < 0:
            print("Invalid input. Please enter a non-negative integer.")
            failed_entries += 1
            add_inventory = False

        # If input is validated proceed to add inventory
        if add_inventory:
            # Check if inventory exceed limit of 500 units
            if inventory > 500:
                print("Overstock inventory limit exceeded. Cannot add more stock.")
                break
            else:
                inventory += int(user_input)
                print(f'Current Inventory: {inventory}')
    except ValueError: # Exception to catch any unexpected errors during conversion e.g. --3
        print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
        failed_entries += 1
        add_inventory = False
