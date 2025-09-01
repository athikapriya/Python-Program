'''
1. Hierarchical Inheritance
2. Multi-level Inheritance
3. Multiple Inheritance
'''

# multilevel inheritance
class A:
    def display1(self):
        print("I am from class A")

class B(A):
    def display2(self):
        print("I am from class B")

class C(B):
    def display3(self):
        super().display1()
        super().display2()
        print("I am from class C")

obj = C()
print(isinstance(obj, B))
obj.display3()

# multiple inheritance
class a :
    def display(self):
        print("I am from class a")

class b:
    def display(self):
        print("I am from class b")

class c(a, b):
    # def display(self):
    #     print("I am from class c") ### this is show the class c for priority
    pass # now result will show from class a, as i choose (a, then b)

myobj = c()
myobj.display()
