myFile = open("Students.txt", "r+")
print(myFile.readable())
print(myFile.writable())

# lines = myFile.readlines()
lines = myFile.readlines()[0]
print(lines)

text = myFile.read()
print(text)

size = len(text) # total character
print(size)


myFile.close()