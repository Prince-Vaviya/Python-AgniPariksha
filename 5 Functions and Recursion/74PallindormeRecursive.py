def is_palindrome(s):
    s = s.lower()  
    if len(s) <= 1:  
        return True
    if s[0] != s[-1]:  
        return False
    return is_palindrome(s[1:-1])  


input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
