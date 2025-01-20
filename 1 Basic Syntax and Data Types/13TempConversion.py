operation = True
while(operation):
    print("1. Celcius to Fahrenheit")
    print("2. Fahrenheit to Celcius")
    print("3. Stop")
    opt = int(input("Enter your option : "))
    if opt == 3:
        operation = False
        break
    if opt == 1:
        cel = float(input("Enter temperature in celcius : "))
        print(f"{cel}C = {1.8 * cel + 32}F")
    elif opt == 2:
        fah = float(input("Enter temperature in fahrenheit : "))
        print(f"{fah}F = {(fah - 32)/1.8}C")
    else:
        print("Invalid input")