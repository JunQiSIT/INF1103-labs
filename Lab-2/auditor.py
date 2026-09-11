inventory = 0

while True:
    try:
        user_input = input("Enter stock quantity (or type 'quit' to exit): ")
        if user_input == 'quit':
            print("Exiting the program.")
            break    
    except ValueError:
        print("Invalid input. Please enter a valid integer or type 'quit' to exit.")
        continue

    