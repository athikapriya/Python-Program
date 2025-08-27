fruits = ["Apple", "Orange", "Mango", "Lichi", "Kiwi"]
print(fruits)

# length of the list
length = len(fruits)
print(f"The length of the list is : {length}")

# data types for list
list1 = ["apple", 1, True]

print(list1)
print(type(list1[0]))
print(type(list1[1]))
print(type(list1[2]))

# creating new list with "List" Constructor
name = ("Athika", "Priya")
name = list(name)
print(name)

# Access List item
print(fruits[2])
print(fruits[-1])
print(fruits[2:6])
print(fruits[:4])
print(fruits[3:])
print(fruits[::-1])
print(fruits[-3:-1])

# check if item exit
if "apple" in fruits:
    print("List item exits.")
else:
    print("Item not exits.")

# change Items
fruits[2] = "Watermelon"
print(fruits)
fruits[1:2] = ["Mango", "Guava"]
print(fruits)
fruits[1:7] = [1, 2, 3]
print(fruits)

# add items
fruits.append("Organge")
print(fruits)
fruits.insert(2, "Banana")
print(fruits)
newFruits = ["pineapple", "papaya", "pineapple",]
fruits.extend(newFruits)
print(fruits)
morefruits = ("Peach", "grapefruit") # add tuples
fruits.extend(morefruits)
print(fruits)

# remove items
fruits.remove("pineapple")
print(fruits)
fruits.pop(2)
print(fruits)
fruits.pop()
print(fruits)
del fruits[0]
print(fruits)
#del fruits          # can delete full list
# fruits.clear()      # clear list
# print(fruits)

# Looping list
for x in fruits:
    print(x)
for i in range(len(fruits)):
    print(fruits[i])

a = 0       # while loop
while a < len(fruits):
    print(fruits[a])
    a += 1

fruits.reverse()
print(fruits)