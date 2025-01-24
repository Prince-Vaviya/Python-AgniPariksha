def find_longest_word(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            words = contents.split()
            for j in range(len(words)):
                for i in range(len(words)-1):
                    if(len(words[i]) < len(words[i+1])):
                        words[i], words[i+1] = words[i+1], words[i]
            print(words[0])
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None


find_longest_word("6 File I:O and Exception Handling/82File.txt")