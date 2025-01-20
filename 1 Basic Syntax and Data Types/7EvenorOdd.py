def Even_Odd(num1):
    if(num1 % 2 == 0):
        print(f"{num1} is Even number")
    else:
        print(f"{num1} is Odd number")

    
num1 = int(input("Enter a number to check Even or Odd : "))
Even_Odd(num1)
