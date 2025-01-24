class Shape:
    def draw():
        print("Who is who ???")
    
class Triangle(Shape):
    def draw(self):
        print("I am Triangle ")

class Circle(Shape):
    def draw(self):
        print("I am Circle ")

class inf:
    def sys(self):
        print("ok")
    
shapes = Circle().draw()
shapes = Triangle().draw()