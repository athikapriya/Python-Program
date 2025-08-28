# Typles is a kind of data structure as list
# but list values can be changed, but tuples values are not
# It's better to use first bracket for tuples, whereas list uses third bracket, dictionaries uses second bracket

students = ("Athika", "Tina", True, 22)
print(students)  # print tuple
print(students[0]) # tuple items index
print(type(students)) # type
print(type(students[0])) # type of index item
print(type(students[3]))

flower = ("rose", ) # tuple with one item should have a comma, otherwise it would be string
print(type(flower))

# access items
fruits = ("apple", "banana", "orange", "mango", "watermelon")
print(fruits[-2])
print(fruits[1:2])
print(fruits[2:])
print(fruits[:4])
print(fruits[::-3])
print(fruits[-4:-3])
for x in fruits:
    print(x)


# Once a tuple is created, you cannot change its values. to change value , we can use list
x = ("kiwi", "lichi")
y = list(x) # convert to list
y[1] = "banana" # change items
y.append("mango") # add items
y = tuple(y) # convert to tuple
print(y)
z = ("Apple", )
total_fruits = y + z
print(total_fruits) # can add two tuple

# remove items
newTuple = list(total_fruits)
newTuple.remove("mango")
newTuple = tuple(newTuple)
print(newTuple)

# del newTuple #totally delete the tuple

### unpack typles
flower = ("rose", "sunflower", "belly", "daisy", "tulip")
(red, yellow, *white) = flower
print(f"{red} is red, {yellow} is yellow, {white} are white")

# looping
for i in range(len(flower)):
    print(flower[i])

# join tuple
print(flower + fruits)
print(flower * 2)

# methods
fruits = fruits.count("apple")
print(fruits)

num = (1, 2, 3)
num = num.index(3)
print(num)