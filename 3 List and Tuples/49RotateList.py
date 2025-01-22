original_list = [1, 2, 3, 4, 5]


k=int(input("Enter number to rotate list : "))

temp = original_list[-k:]
for i in range(k):
    original_list.pop()

print(temp + original_list)
