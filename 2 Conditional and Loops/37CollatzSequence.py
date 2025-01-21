num = int(input("Enter a number : "))
print(num)

while num != 1:
    if num % 2 == 0:
        num = num // 2
        print(num)
    elif num % 2 != 0:
        num = (num * 3) + 1
        print(num)