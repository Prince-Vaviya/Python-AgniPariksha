class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age

person1 = person("Mr.Eagle", 20)
print("Name:", person1.get_name())
print("Age:", person1.get_age())

person1.set_name("Mr.Eagle1")
person1.set_age("20.0")
print("Name:", person1.get_name())
print("Age:", person1.get_age())