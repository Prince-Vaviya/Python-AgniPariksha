class Car:
    def __init__(self, make="TATA", model="Nano", year=2020):
        self.make = make
        self.model = model
        self.year= year
    def display(self):
        print(f"The make of the car is : {self.make} ")
        print(f"The model of the car is : {self.model} ")
        print(f"The manufacture year of the car is : {self.year} ")

car1 = Car("Maruti", "Maruti_800", 2022)
car1.display()

car2 = Car()
car2.display()