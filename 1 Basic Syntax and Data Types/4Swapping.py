a = int(input("Enter a number : ")) 
b = int(input("Enter another number : "))
print(f"Before Swapping a = {a} and b = {b}")

a = a + b
b = a - b 
a = a - b 

print(f"After Swapping a = {a} and b = {b}")