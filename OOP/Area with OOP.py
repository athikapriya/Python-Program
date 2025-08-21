base = float(input("enter base : "))
height = float(input("enter height : "))

class areaOfShapes:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        print("I am area method of areaOfShapes class")


class triangle(areaOfShapes):
    def calculate_area(self):
        area = (self.base * self.height) * 1/2
        print(f"Area of triangle : {area}")

class square(areaOfShapes):
    def calculate_area(self):
        area = (self.base * self.height)
        print(f"Area of square : {area}")

x = triangle(base, height)
x.calculate_area()

y = square(base, height)
y.calculate_area()