operation = True
while(operation):
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Stop")
    opt = int(input("Enter a number : "))
    if opt == 5:
        operation = False
        break
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    if opt == 1:
        print(f"Sum of {num1} and {num2} is {num1+num2}")
    elif opt == 2:
        print(f"Difference of {num1} and {num2} is {num1-num2}")
    elif opt == 3:
        print(f"Product of {num1} and {num2} is {num1*num2}")
    elif opt == 4:
        if num2 == 0:
            print("Zero Division Error")
        else:
            print(f"Quotient of {num1} and {num2} is {num1/num2}")
    else:
        print("Invalid input")