class Phone:
    def __init__(self):
        print(f"This is phone class.")

class sumsung(Phone):
    def __init__(self): # this is actually overriding,
                        # as we used the same constructor here like parent class phone

        super().__init__() # we can use super class property with this
        print("This is sumsung class.")

p = sumsung()

## shape of triangle and rectangle

base= int(input("Enter the base : "))
height = int(input("Enter the height : "))

class shape:
    def __init__(self, base, height):
        self.height = height
        self.base = base

    def area(self):
        print("This is area of shpae calss.")

class Triangle(shape):
    def area(self):
        area = 0.5 * self.base * self.height
        print(f"Area of Triangle : {area}")

class Rectangle(shape):
    def area(self):
        area = self.base * self.height
        print(f"Area of Rectangle : {area}")

triangle = Triangle(base, height)
triangle.area()

rectangle = Rectangle(height, base)
rectangle.area()