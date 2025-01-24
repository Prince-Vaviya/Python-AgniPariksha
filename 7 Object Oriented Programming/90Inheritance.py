class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def tail():
        print("They have tail")

    def info(self):
        print(f"{self.name} is the name ")
        print(f"{self.breed} is the breed ")
    

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed)
    
    def tail():
        print("Woof Woof")
    
    def info(self):
        return super().info()

D = Dog("Rocket","Husky" )
print(D.info())

