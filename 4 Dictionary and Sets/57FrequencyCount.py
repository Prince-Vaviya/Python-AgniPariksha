def count_frequency(lst):
    """Count the frequency of each element in the list."""
    frequency = {}  

    for item in lst:
        if item in frequency:
            frequency[item] += 1  
        else:
            frequency[item] = 1  

    return frequency

def main():

    sample_list = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6]
    
    frequency_count = count_frequency(sample_list)
    print("Frequency count of elements in the list:")
    for element, count in frequency_count.items():
        print(f"{element}: {count}")

if __name__ == "__main__":
    main()