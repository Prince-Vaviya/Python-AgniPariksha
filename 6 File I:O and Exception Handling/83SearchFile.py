def search_in_file(filename, substring):
    try:
        with open(filename, 'r') as file:
            search_line = []
            for line in file:
                if substring in line:
                    search_line.append(line)
            
            for i in range(len(search_line)):
                print(search_line[i])



    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []


substring = input("Enter the substring to search for: ")
search_in_file("6 File I:O and Exception Handling/83Text.txt", substring)

