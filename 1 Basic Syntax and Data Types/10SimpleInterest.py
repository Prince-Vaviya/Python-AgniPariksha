def simple_interest(principal, tenure, interest):
    print(f"The Simple Interest is {(principal * tenure * interest)/100} ")
    
    
principal = float(input("Enter the principal amount : "))
tenure = float(input("Enter no. of years : "))
interest = float(input("Enter the rate of interest : "))

simple_interest(principal, tenure, interest)
