def copy_file(source, destination):
    with open(source, 'r') as src_f:
        contents = src_f.read()
    with open(destination, 'w') as dest_f:
        dest_f.write(contents)
    print(f"Copied contents from {source} to {destination}.")

copy_file('6 File I:O and Exception Handling/source.txt', '6 File I:O and Exception Handling/destination.txt') 
