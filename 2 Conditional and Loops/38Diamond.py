def print_diamond(width):
    for i in range(width):
        print(' ' * (width - i - 1), end='')
        print('*' * (2 * i + 1))

    for i in range(width - 1):
        print(' ' * (i + 1), end='')
        print('*' * (2 * (width - i - 2) + 1))


width = int(input("Enter the width of the diamond: "))

print_diamond(width)
