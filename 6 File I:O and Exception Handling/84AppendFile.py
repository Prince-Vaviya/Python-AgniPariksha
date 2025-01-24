def append_to_file(filename):
    line = input("Enter a line to append to the file: ")
    try:
        with open(filename, 'a') as file:
            file.write(line + '\n')
        print(f"Appended to '{filename}'.")
    except IOError:
        print(f"Error: An I/O error occurred while appending to the file '{filename}'.")

append_to_file("6 File I:O and Exception Handling/Text84.txt")
