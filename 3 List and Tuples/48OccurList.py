list1 = [1, 2, 3, 4, 5, 6, 7, 3]
count = 0

ele = int(input("Enter number to be checked : "))

for i in list1:
    if i == ele:
        count += 1

print(count)