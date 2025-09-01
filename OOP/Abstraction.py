from abc import ABC,abstractmethod

class shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass # if a method doesn't have body, that is abstract method
            # and the class which uses abstraction method is called abstraction class, here shpae is abstract class

class rectangle(shape):
    # if a class inherit abstract class, it must use their abstract methods
    def area(self):
        area = self.dim1 * self.dim2
        print(f"The area of the rectangle is {area}")

# if a abstract class is created, you can't call the abstract method
# s1 = shape(1, 2)
# s1.area()

r1 = rectangle(20, 10)
r1.area()