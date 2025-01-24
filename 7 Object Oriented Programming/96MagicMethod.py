class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

def main():
    person1 = Person("Alice", 30)
    
    print(person1)

if __name__ == "__main__":
    main()