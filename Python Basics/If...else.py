# talking user input
# with if...else, test letter grade mark

num = int(input("enter num : "))

if num <= 0 or num > 100:
    print("invalid number")
elif 80 <= num <= 100:
    print("A+")
elif 70 <= num <= 79:
    print("A")
elif 60 <= num <= 69:
    print("A-")
elif 50 <= num <= 59:
    print("B")
elif 40 <= num <= 49:
    print("C")
elif 33 <= num <= 39:
    print("D")
else:
    print("Fail")