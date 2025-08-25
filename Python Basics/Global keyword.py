# generally all variable outside the function is globla variable

# make a variable global inside a function
x =  "this is x"
def myfunc():
    global x
    x = x.capitalize()
    print(f"{x}, It's a global variable inside a function.")
myfunc()

# change a global variable value inside a function
name = "athika"
def myname():
    global name
    name = 'athika chowdhury priya'
    name = name.capitalize()

myname()
print(f"\nMy full name is {name}.The value is changed.")