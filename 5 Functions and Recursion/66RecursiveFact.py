def Factorial(num):
    if num == 0 or num == 1:
        return 1
    
    else:
        return num * Factorial(num-1)
        
    
print(Factorial(5))
