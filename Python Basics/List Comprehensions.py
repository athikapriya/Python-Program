'''
syntax
    [ expression for item in list ] , or you can say [ expression forLoop ]
'''

num = [1, 2, 3, 4, 5]

square = [x * x for x in num]
print(square)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newfruits = [x for x in fruits if "a" in x]
print(newfruits)
freshFruits = [x.upper() for x in fruits if x != "mango"]
print(freshFruits)