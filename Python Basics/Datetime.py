import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)

print(x.strftime("%A"))
x = x.strftime("%H:%M %p")

print(f"It's {x}")


# creating data objects
x = datetime.datetime(2024, 6, 8)
print(x)
print(x.strftime("%B"))
