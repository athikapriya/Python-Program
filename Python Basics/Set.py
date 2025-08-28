# set is also a data structure
# Set is an unordered collection of item, so values can't be accessible by index number
# Can't take duplicate values
# Use curly braces {}, or set function

set1 = {"apple", True, 33, False, 0} # false and 0 are considered the same value
print(set1)
print(type(set1))

print(len(set1))
set2 = set(("mango", "lichi")) # constructor set
print(set2)

# access items
for x in set2:
    print(x)

print("mango" in set1) # checks if  mango is in set1

# add items
set2.add("Kiwi")
print(set2)

# add sets
set1.update(set2) # adding set1 and set2
print(set1)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
fruits = {"apple", "banana", "cherry"}
tuple = ("rose", "belly") # tuple
list = [1, 3, 5] # list
fruits.update(tuple)
print(fruits)
fruits.update(list)
print(fruits)

# remove items
fruits.remove('banana')
print(fruits)

fruits.discard("rose") # remove and discard works as same
print(fruits)

fruits = fruits.pop() # pop can remove any item, not fixed one
print(fruits) # the value of pop is the removed item

#fruits.clear() # clear the set
# del fruits # del deletes the set

# # # join sets
num1 = {1, 2, 3}
num2 = {4, 5, 6}
num3 = num1.union(num2)  # update and union join sets
print(num3)
num4 = {8, 9}
num5 = num3 | num4 # union can use with union keyword or " | " operator
print(num5)

new_number= num1.union(num2, num4)
print(new_number)

# The intersection() method keeps ONLY the duplicates.
flower1 = {'rose', "belly"}
flower2 = {"belly", "daisy"}
myflower = flower1.intersection(flower2)  # can use "&" operator
print(myflower)

# intersection update
flower1.intersection_update(flower2)
print(flower1)

'''
The values True and 1 are considered the same value. The same goes for False and 0
'''

tech = {'apple', 'microsoft', "amazon"}
fruit = {"apple", "banana", "cherry"}
print(tech - fruit) # difference

tech.difference_update(fruit)
print(tech)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
newSet = tech.symmetric_difference(fruit) # can also use " ^ " operator
print(newSet)

print(tech.symmetric_difference(fruit))