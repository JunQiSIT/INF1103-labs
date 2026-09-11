inventory = 0

while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit): ")

    if user_input == 'quit':
        print("Exiting the program.")
        break    

    # Checks if the input is a valid integer ignoring the negative sign for validation
    # Afterwards converts user input string to an integer and checks if it is non-negative
    try:
        if not user_input.lstrip('-').isdigit():
            print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
        elif int(user_input) < 0:
            print("Invalid input. Please enter a non-negative integer.")
    except ValueError: # Exception to catch any unexpected errors during conversion e.g. --3
        print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
     

    