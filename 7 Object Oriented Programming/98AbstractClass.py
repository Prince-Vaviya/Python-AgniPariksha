from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

def main():
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print(f"Area of Circle: {circle.area():.2f}")
    print(f"Area of Rectangle: {rectangle.area()}")

if __name__ == "__main__":
    main()