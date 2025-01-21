string = input("Enter a string : ")
letter = input("Enter a character that need to be counted : ")
count = 0

for i in string:
    if i == letter:
        count += 1

print(f"Total {count} times the character '{letter}' occurred")