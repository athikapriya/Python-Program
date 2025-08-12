# 1 + 2 + 3 + .....+ n
n = int(input("Enter n number : "))
sum = 0

for index in range(1, n+1, 1): # start, ending, interval
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
for index in range(1, n+1):
    square = index * index
    # print(square)
    sum = sum + square
print(sum)