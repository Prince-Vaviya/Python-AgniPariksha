def prime(num1):
    for i in range(2, int((num1+1)/2)):
        if(num1%i==0):
            print(f"{num1} is not prime number ")
            break
    else:
        print(f"{num1} is a prime number ")

num1 = int(input("Enter a number to check : "))
prime(num1)