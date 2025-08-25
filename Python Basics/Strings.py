# Multiline Strings
# Multiline Strings should be inside 3 quotation , either its single or double

rhyme = ''' 
Johney Johney
Yes papa,
Eating Sugar ?
No papa. 
Telling Lies ?
No papa.
Open Your Mouth
Ha Ha Ha.
'''

print(rhyme)

# Strings are Arrays
text = "hello", "world"
print(text[1])

# Looping Through a String
letter = "banana"
for x in letter:
    print(x)

# check string
line = "this is a single line."
print("single" in line)
print("single" not in line)
print("name" in line)

# using if statement
if 'name' not in line:
    print(f"The keyword 'name' is not in line.")

# slicing string using colon
print(line[3:20])
print(line[:7]) # slice from the start
print(line[3:]) # slice to the end
print(line[-19:-4]) # negative indexing


# modify
name = "athika chowdhury priya                          "
print(name.capitalize().strip()) # modify white space, and capitalize
print(name.replace("priya", " ")) # replace

text1 = "hello world"
print(text1.split(",")) # returns list

# format string placeholder and modifier
a = 20
print(f"The result is {a * 20}")
print(f"The result is {a:.2f}")