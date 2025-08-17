name = "Athika Priya"
age = 20
university = "Bangladesh University Of Professioanls"

print("My name is " + name + ".") # string can be added by "+" sign
print("I am" ,age , "years old.") # numbers should be added by ", ,"
print("My University : " + university +  ".") # string

# Using Backslash
print("I am " + name + ". \nI am ",age," years old. \nI am currently studying at " + university + "."  )

'''
where " \n " specify a new line
" \t "  specify 4 spaces
'''

# Text type : str
print("\n=== Text Data types ===")
name = "Athika Priya"
print(type(name))

# Numeric type : int, float, complex
print("\n=== Numeric Data types ===")
num1 = 2
num2 = 3.5
num3 = 2j
print(type(num1))
print(type(num2))
print(type(num3))

# Sequence type : list, tuple, range
print("\n=== Sequence Data types ===")
list = ["apple", "banana", "cherry"]
tuple = ("apple", "banana", "cherry")
range = range(5)
print(type(list))
print(type(tuple))
print(type(range))

# Mapping type : dict
print("\n=== Mapping Data types ===")
dict = {
    "name" : "Athika Priya",
    101 : "Section A",
    "numbers" : (1, 2, 3, 4), # tuple as value
    "skills" : ["python", "Java"], # list as value
    "extra" : {
        "a" : 1,
        "b" : 2,
    } # dict as value
}
print(type(dict))

# Set type : set, frozenset
print("\n=== Set type Data types ===")
set ={ "apple", "banana", "cherry" }
print(type(set))

frozenset = frozenset({"apple", "banana", "cherry"})
print(type(frozenset))

# Boolean type : bool
print("\n=== Boolean Data types ===")
bool = False # True or False should be start with Capital letter
print(type(bool))

# Binary type : byte, bytearray, memoryview
print("\n=== Binary Data types ===")
binary = b"hello" # add 'b' in front of the str
print('\n',binary)
print(type(binary))

bytearray = bytearray(5)
print('\n',bytearray)
print(type(bytearray))

memoryview = memoryview(bytes(5))
print("\n",memoryview)
print(type(memoryview))

# None type : none
print("\n=== None type Data types ===")
x = None
print(type(x))