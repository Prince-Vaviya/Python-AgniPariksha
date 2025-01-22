list1 = [1, 2, 5, 3, 0]
list2 = []

for i in range(-1, -len(list1) - 1, -1):
    list2.append(list1[i])


print(list2)