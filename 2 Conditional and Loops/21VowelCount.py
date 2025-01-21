string = input("Enter string : ")
count = 0

for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
if count == 1:
    print(f"There are total {count} vowel in given string")
else:
    print(f"There are total {count} vowels in given string")