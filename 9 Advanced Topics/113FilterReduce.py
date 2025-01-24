from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

sum_of_odds = reduce(lambda x, y: x + y, odd_numbers)

print("Odd numbers:", odd_numbers)
print("Sum of odd numbers:", sum_of_odds)
