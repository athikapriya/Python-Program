'''
syntax
    [ expression for item in list ] , or you can say [ expression forLoop ]
'''

num = [1, 2, 3, 4, 5]

square = [x * x for x in num]
print("Square : " , square)

mod = [x for x in num if x % 2 == 0] # used filtering here
print(mod)