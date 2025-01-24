class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def disp(self):
        print(f"{self.length} and {self.length}")

s = Square(20)
s.disp()

