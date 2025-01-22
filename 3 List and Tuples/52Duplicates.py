list1 = [1, 2, 5, 7, 3, 7, 7, 3, 1, 2]
for i in list(set(list1)):
    count = 0
    for j in list1:
        if i==j:
            count += 1
        
    if count >= 2:
        print(i)

