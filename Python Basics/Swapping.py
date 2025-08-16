a = 20
b = 10
'''
temp = a # temp = 20
a = b # a = 10
b = temp # b = 20
'''

a, b = b, a
print(f"a = {a}, b = {b}")