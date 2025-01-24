def word_count(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            words = contents.split()
            print(f"The file {filename} has {len(words)} words.")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")


word_count('6 File I:O and Exception Handling/text79.txt')
