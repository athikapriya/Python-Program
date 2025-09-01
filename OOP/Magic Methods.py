# methods that have double underscore before and after ,like __init__
'''
Magic methods for comparison
    __lt__ for <
    __le__ for <=
    __eq__ for ==
    __ne__ for !=
    __gt__ for >
    __ge__ for >=
'''

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name : {self.name}, Age : {self.age}"

    def __eq__(self,other):
        return self.name == other.name and self.age == other.age

    def display(self):
        print(f"Name : {self.name}, Age : {self.age}")

s1 = student("athika",20)
s2 = student("athika",20)

# str method
print(s1)

# equal method
print(s1 == s2)