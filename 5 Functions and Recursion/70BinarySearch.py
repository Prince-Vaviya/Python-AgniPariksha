def binary_search(arr, target, low, high):

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high) 
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return -1 



sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter the number to search for: "))

result = binary_search(sorted_list, target, 0, len(sorted_list) - 1)

if result == -1:
    print(f"Element {target} not found in the list.")
else:
    print(f"Element {target} found at index: {result}")