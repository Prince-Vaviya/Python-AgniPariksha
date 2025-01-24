import csv

def read_csv_file(filename):

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"Error: An error occurred while reading the file: {e}")
    
read_csv_file("6 File I:O and Exception Handling/85File.csv")
