class A:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def __add__(self):
        print(f"x = {self.x1 + self.x2}, y = {self.y1 + self.y2}")

a = A(10, 5, 5, 10)
a.__add__()