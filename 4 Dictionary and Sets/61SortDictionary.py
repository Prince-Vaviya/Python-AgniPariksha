def sort_dict_by_value(sample_dict):

    sorted_dict = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
    return sorted_dict



sample_dict = {'apple': 3, 'banana': 1, 'orange': 2, 'grape': 4 }

print("Original dictionary:")
print(sample_dict)


print("Sorted dictionary by values (ascending order):")
print(sort_dict_by_value(sample_dict))