'''
1. Hierarchical Inheritance
2. Multi-level Inheritance
3. Multiple Inheritance
'''


class A:
    def display(self):
        print("I am from class A")

class B:
    def display(self):
        print("I am from class B")

class C(A, B):
    pass

obj = C()
print(isinstance(obj, B))
obj.display()
