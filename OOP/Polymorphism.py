# Built-in polymorphic function
# when a function performs same for different data types like len function
print(len("Athika Priya"))
print(len([1, 2, 3, 4]))

# user defined polymorphic function
def add(x, y, z = 0):
    return x + y + z

print(add(2, 4))
print(add(2, 4, 5))