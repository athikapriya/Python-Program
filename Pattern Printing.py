'''
if n = 3, print
*
**
***
'''
n = int(input("enter n number  : "))
for index in range(n + 1):
    print(index * " * ")


'''
*
***
*****
'''
n = int(input("enter n number  : "))
for index in range(n + 1):
    print((2 * index -1) * " * ")