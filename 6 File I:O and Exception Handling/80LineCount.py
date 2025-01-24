def line_count(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(f"The file {filename} has {len(lines)} lines.")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")


line_count('6 File I:O and Exception Handling/80example.txt') 

