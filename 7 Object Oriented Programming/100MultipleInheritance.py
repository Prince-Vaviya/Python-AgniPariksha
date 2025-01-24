class Shape:
    def method_a(self):
        return "I am Shape"

class Rectangle:
    def method_b(self):
        return "I am class Rectangle"

class Square(Shape, Rectangle):
    def method_c(self):
        return "I am class Square"

obj = Square()
print(obj.method_a()) 
print(obj.method_b()) 
print(obj.method_c()) 