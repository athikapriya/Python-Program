#  === the init method === can call itself
class person :
    def __init__(self, name, age):
        self.name =  name
        self.age = age

Rittika = person("Rittika", 18)
print(f"Name: {Rittika.name}. Age: {Rittika.age}")


# === str method ===
class subjects:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def __str__(self):
        return f"Book Name : {self.name}. Group : {self.group}"

Chemistry = subjects("Chemistry", "Science")
print(Chemistry)


# === create method ===
class Girls:
    fullName = ""
    roll = ""
    university = ""

    def set_value(self, fullName, roll, university): # here we can also use init method
        self.fullName = fullName
        self.roll = roll
        self.university = university

    def details(self): # can use selfmade function method instead of str method
        print(f"Full Name : {self.fullName}. Roll : {self.roll}. University : {self.university}.")

athika = Girls()
athika.set_value("Athika Chowdhury", 1, "Bangladesh University of Professionals")
athika.details()

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class


# === modify object parameters ===
class color:
    def __init__(self, r, g, b, p):
        self.r = r
        self.g = g
        self.b = b
        self.p = p

    def __str__(self):
        return f"Red = {self.r}, Green = {self.g}, Blue = {self.b} makes the color White"

prefered_color = color(255, 0, 0, 0)
prefered_color.g = 255 # modify object
prefered_color.b = 255
del prefered_color.b # delete object
print(prefered_color)


# === the pass statement
class Person:
  pass # having an empty class definition like this, would raise an error without the pass statement
