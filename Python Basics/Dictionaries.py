# dictionary is a data structure for python

student1  = {
    "name" : "athika",
    "age" : 28,
    "cgpa" : 3.92,
    "year" : 2025,
    "year" : 2020, # duplicates are not applicable, only last value will show
    "colors" : ["red", "green", "blue"],
    "serial" : {1, 3, 5} # nested dict
}

print(student1)
print(type(student1))

print(student1["name"])
print(student1.get("name"))

print(len(student1))

# dict constructor
student2 = dict(name = "rittika", age = 22)
print(student2)

# access items
print(student1.keys())  # only gives the keys
print(student1.values()) # only gives values
print(student1.items()) # shows both keys and values

# check if key exits
if "age" in student1 :
    print("Yes, age is in the dictionary")

# update or change dictionary
student1.update({"language" : "Python"})
print(student1)

# add items
student1["subject"] = "CSE"
print(student1)

# remove items
student1.pop("language") # pop specified item
print(student1)

student1.popitem()
print(student1) # pop last item

del student1["year"]
print(student1) # delete specific key value

# del student1  # delete full dictionary
# student.clear()

# copy dict
student3 = student1.copy() # can also use dict keyword
print(student3)