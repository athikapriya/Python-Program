# Recursion is a process where a function can call itself
# To stop calling, we need a base case
'''
2 important case in case of recursion
    1. Recursive call
    2. Base Case
'''

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))