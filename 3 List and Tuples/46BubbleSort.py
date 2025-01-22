l1 = [2, 5, 6, 8, 3, 1]

for j in range(len(l1)):
    for i in range(0, len(l1)-1):
        if l1[i] > l1[i+1]:
            l1[i], l1[i+1] = l1[i+1], l1[i]

print(l1)