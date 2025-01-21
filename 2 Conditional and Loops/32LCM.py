
def lcm(a, b):
    alist1 = []
    blist2 = []
    for i in range(1, b+1):
        alist1.append(a*i)
    
    for j in range(1, a+1):
        blist2.append(b*j)

    for i in alist1:
        for j in blist2:
            if i == j:
                print(f"LCM of {a} and {b} is {i}")
    


num1 = int(input("Enter a positive integer : "))
num2 = int(input("Enter a positive integer : "))
lcm(num1, num2)
