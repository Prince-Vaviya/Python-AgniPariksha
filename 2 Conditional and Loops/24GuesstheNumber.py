import random

num = random.randint(1, 11)

num1 = int(input("Guess the number : "))
if num1 == num:
    print("Wohoo, You guessed it correct ")
else:
    print("Incorrect")