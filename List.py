list = ["C", "C++", "Java", "Python", "Ruby", "Scala"]

print(list) # all the list items
print(list[3]) # index number 3 (python)
print(list[3:]) # starts from index 3
print(list[2:4]) # starts from index 2 , and will show 4-2 = 2 items
print(list[-1])  # reverse the items

print("C" in list) # true
print("python" in list) # false , as python is written as Python in the list. It's case-sensitive
print("Swift" not in list) # true

print(list + ["Kotlin", 27]) # add items
print(list * 3) # shows 3 times of these items

print(len(list)) # shows length of the list items
list.append("BASIC") # append item at the end
print(list)

list.insert(2, "Fortran") # insert items following the index number
print(list)

list.remove("BASIC") # remove item
print(list)

list.sort() # sort items according to the alphabetic order
print(list)

list.reverse() # reverse item according to the alphabetic order
print(list)

list.pop() # remove list item
print(list)

position = list.index("C++") # shows index number of the item
print(position)

languages = list.copy() # copy items
print("languages : " , languages)

count = list.count("Java") # shows how many times Java is in the list
print(count)

list.clear() # clear all items
print(list)