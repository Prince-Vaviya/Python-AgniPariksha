list1 = [1, 2, 3, 4, 5, 6]
num = int(input("Enter a number to find : "))

if num in list1:
    print(list1.index(num))
else:
    print(-1)