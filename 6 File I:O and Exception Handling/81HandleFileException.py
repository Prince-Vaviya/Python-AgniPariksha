def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")



read_file("6 File I:O and Exception Handling/example.txt")