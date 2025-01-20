def compound_interest(principal, tenure, interest):
    print(f"The Compound Interest is {(principal * (1+interest) ** tenure) - principal} ")
    


principal = float(input("Enter the principal amount : "))
tenure = float(input("Enter no. of years : "))
interest = float(input("Enter the rate of interest : "))/100

compound_interest(principal, tenure, interest)
