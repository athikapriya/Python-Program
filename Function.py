# there are two types of function
# 1. Library function ( ready function ), they carry first bracket with them >> print(), input()
# 2. User defined function (  )

x = int(input("Enter x : "))
y = int(input("Enter y : "))
def add(x, y):
    sum = x + y
    print(sum)

add(x, y)

def add2(x, y, z):
    sum = x + y + z
    print(sum)
add2(x,y, 5)

# function without parameter
def result():
    print("there's no parameter.")

result()