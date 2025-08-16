# Runtime Error/Incorrect Input/Incorrect code
# try and except keyword


try:
    list = [10, 30, 50, 0]
    # div = list[0] / list[3] # this one is devided by 0, so its ZeroDivisionError
    div = list[0] / list[5] # this one is out of range, so its indexError
    print(div)
except ( ZeroDivisionError, IndexError ) : # multiple exception in 1 line, also can handle individually
    print("Incorrent Input")

finally: # the codes under finally must work
    print("Closing the program")


## raise keyword

def voter(age):
    if age < 18:
        raise ValueError("incorrect age")
    return "You are allowed to vote"


try:
    print(voter(17))
except ValueError as e:
    print(e)