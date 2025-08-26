print(10 > 3)
print(10 < 8)
print(10 <= 5)

# Evaluate Values and Variables
print(bool("hello"))
a = bool("")
print(f"empty string with no space gives boolen : {a}")
b = bool(" ")
print(f"empty string with space gives boolean : {b}")
c = bool(33)
print(f"any number expect 0 gives boolean : {c}")
d = bool(0)
print(f"number 0 gives boolean : {d}")
fruits = ["apple", "banana", "cherry"]
fruits = bool(fruits)
print(f"any list, tuple, set , and dictionaries are {fruits}, expect empty ones.")

print(f"\nfalse values are also none, False")
print(bool(None))
print(bool(False))

class myclass:
    def __len__(self):
        return 0

myobj = myclass()
x = bool(myobj)
print(f"if an object of a class has a __len__ function, and that returns 0, it's also {x}")

name = "Athika"
print(isinstance(name, str))
print(isinstance(name, int))

