# set is also a data structure
# Set is an unordered collection of item, so values can't be accessible by index number
# Can't take duplicate values
# Use curly braces {}, or set function

num1 = {1, 2, 3, 4, 5, 5} # won't print last value 5, as it's repeated
num2 = set([4, 5, 6]) # [4, 5, 6] are on a list, stored in a set using set function

print(num1)
print(num2)

num2.add(7) # add items
num2.remove(4) # remove items
print(num2)

print(7 in num2) # check if 7 is in num2
print(7 not in num2)

print(num1 | num2) # union sets (print all values ingoring repeated ones)
print(num1 & num2) # intersection (print common values)
print(num1 ^ num2)
print(num1 - num2) # difference (print only different values)