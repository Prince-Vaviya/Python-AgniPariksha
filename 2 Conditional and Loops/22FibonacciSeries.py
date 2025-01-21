n1, n2 = 0, 1
num = int(input("Enter a number : "))

print(n1)
print(n2)

for i in range(2, num):
    n3 = n2 + n1
    print(n3)
    n1 = n2
    n2 = n3

