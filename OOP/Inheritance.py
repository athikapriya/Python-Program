# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is called base class.
# Child Class is called derived class.

class sectionA:
    def roll1(self):
        print("Anika")

    def roll2(self):
        print("Sara")

class SectionB(sectionA):
    def roll3(self):
        print("Satabdi")

a = sectionA()
a.roll1()
a.roll2()
b = SectionB()
b.roll3()
b.roll1()


print(issubclass(SectionB, sectionA))

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print(self.name, self.age)

class Student(person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def welcome(self):
        print(f'Welcome {self.name}, a {self.age} years old boy who got {self.grade} !')


s = Student("John", 22, "A+")
s.printName()
print(s.grade)
s.welcome()

