# 1 + 2 + 3 + .....+ n
n = int(input("Enter n number : "))
sum = 0
for index in range(1, n + 1, 1): # start, ending, interval
    sum = sum + index
print(sum)


# 2 + 4 + 6 + ... + n
n = int(input("Enter n number : "))
sum = 0
for index in range(2, n + 1, 2):
    sum = sum + index
print(sum)


# 1 + 3 + 5 + ... + n
n = int(input("Enter n number : "))
sum = 0
for index in range(1, n + 1, 2):
    sum = sum + index
print(sum)


# 4 + 8 + 12 + ... + x
x = int(input("Enter x number : "))
sum = 0
for index in range(4, x + 1, 4):
    sum = sum + index
print(sum)



# 1*1 + 2*2 + 3*3 + ... + n*n
n = int(input("Enter n number : "))
sum = 0
for index in range(1, n + 1):
    square = index * index
    sum = sum + square
print(sum)


# 2 * 2 + 4 * 4 + 6 * 6 + n * n
n = int(input("Enter n number : "))
sum = 0
for index in range(2, n + 1, 2):
    square = index * index
    sum = sum + square
print(sum)


# 1 + 1/2 + 1/3 + ... + 1/n
n = int(input("Enter n number : "))
sum = 0
for index in range(1, n + 1):
    sum = sum + 1/index
print(sum)


# 2 * 4 * 6 * ... * n
n = int(input("enter n number : "))
product = 1
for index in range(2, n + 1, 2):
    product  = product * index
print(product)


# 1 * 3 * 5 * 7 * ... * n
n = int(input("Enter n number : "))
product = 1
for index in range(1, n + 1, 2):
    product = product * index
print(product)


# 4 * 8 * 12 * ... * n
n = int(input("Enter n Number : "))
product = 1
for index in range(4, n + 1, 4):
    product = product * index
print(product)


# 1*1 * 2*2 * 3*3 * ... * n*n
n = int(input("Enter n number : "))
product = 1
for index in range(1, n + 1):
    square = index * index
    product *= square
print(product)


# 2*2 * 4*4 * 6*6 * ... * n*n
n = int(input("Enter n number : "))
product = 1
for index in range(2, n + 1, 2):
    square = index * index
    product = product * square
print(product)