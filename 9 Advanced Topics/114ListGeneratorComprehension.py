
list_comp = [x * 2 for x in range(1000000)]
print("List comprehension created a list of length:", len(list_comp))

gen_exp = (x * 2 for x in range(1000000))
print("Generator expression created a generator.")

print("Generator expression converted to list of length:", len(list(gen_exp)))
