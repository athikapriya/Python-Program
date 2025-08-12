# talking user input
# with if...else, test letter grade mark

num = int(input("enter num : "))

if num <= 0 or num > 100:
    print("invalid number")
elif num >= 80 or num == 100:
    print("A+")
elif num >= 70 and num <= 79:
    print("A")
elif num >= 60 and num <= 69:
    print("A-")
elif num >= 50 and num <= 59:
    print("B")
elif num >= 40 and num <= 59:
    print("C")
elif num >= 33 and num <= 39 :
    print("D")
else:
    print("Fail")