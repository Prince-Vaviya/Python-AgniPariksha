def contextManager(fileName):
    with open(fileName, 'w') as file:
        content = input("Enter the content : ")
        file.write(content+ '\n')
        print("Your file was updated")
    

contextManager('116File.txt')
    