def sum_ele(list1, index=0):
    if index >= len(list1):
        return 0
    else:
        return list1[index] + sum_ele(list1, index+1)


print(sum_ele([1, 2, 3, 4]))