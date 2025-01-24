def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if type(item) == list:
            flat_list.extend(flatten(item)) 
        else:
            flat_list.append(item) 
    return flat_list


nested_list = [1, [2, 3], [4, [5, 6]], 7]
print("nested_list ", nested_list)
print("Flattened list:", flatten(nested_list))
