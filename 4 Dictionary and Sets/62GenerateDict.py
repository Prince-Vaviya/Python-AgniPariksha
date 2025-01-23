def generate_dict(n):
    return {i+i:i ** 2 for i in range(1, n + 1)}

n = int(input("Enter a number n: "))

square_dict = generate_dict(n)

print("Generated dictionary of squares: ", square_dict)

