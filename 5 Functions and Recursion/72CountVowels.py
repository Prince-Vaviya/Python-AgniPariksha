def vowel_count(s):
    count = 0
    for i in s.lower():
        if i in ['a', 'e', 'i', 'o', 'u'] :
            count+=1
    return count

str1 = input("Enter a string: ")
print(f"The number of vowels in the string is: {vowel_count(str1)}")

