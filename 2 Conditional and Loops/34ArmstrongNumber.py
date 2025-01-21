num = input("Enter a number : ")
sum = 0

for i in num:
    sum = sum + (int(i) ** len(num))

if int(num) == sum:
    print(f"{num} is an Armstrong number ")
else:
    print(f"{num} is not an Armstrong number ")