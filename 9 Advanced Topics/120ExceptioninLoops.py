
while True:
    user_input = input("Please enter a number: ")
    try:
        number = float(user_input) 
        print(f"You entered a valid number: {number}")
        break  
    except ValueError:
        print("Invalid input! Please enter a valid number.")