class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(f"Temperature in Celsius: {temp.celsius}")
print(f"Temperature in Fahrenheit: {temp.fahrenheit}")


temp.celsius = 30
print(f"Updated Temperature in Celsius: {temp.celsius}")
print(f"Updated Temperature in Fahrenheit: {temp.fahrenheit}")

