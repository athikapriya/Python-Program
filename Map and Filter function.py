# works specially with list or iterable function

## map function
def square(x):
    return x * x

num = [1,2,3,4,5]

result = list(map(square, num))
print(result)

## filter function
num2 = [6, 7, 8, 9]

def mod(y):
    if y % 2 == 0:
        return y

result = list(filter(mod, num2))
print(result)