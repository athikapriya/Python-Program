base = float(input("enter base : "))
height = float(input("enter height : "))

class areaOfShapes:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        Area_of_Triangle = 1/2 * (self.base * self.height)
        Area_of_Square = (self.base * self.height)
        return f"Area of Triangle :  {Area_of_Triangle}. Area of Square : {Area_of_Square}"



area = areaOfShapes(base, height)
print(area.calculate_area())
