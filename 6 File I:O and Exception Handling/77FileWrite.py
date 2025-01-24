def write_file(filename):
    line = input("Enter a line of text: ")
    with open(filename, 'w') as file:
        file.write(line)


write_file('6 File I:O and Exception Handling/77text.txt')