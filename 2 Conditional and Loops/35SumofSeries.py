num = int(input("Enter a number : "))
sum = 0

for i in range(1, num + 1):
    sum += 1/i

print(f"The sum of series is {sum}")