# sub(pattern, replace, string)

import re

pattern = r"color"
text = "Rose is red, it is my favourite color. The color of blood is also red."

text2 = re.sub(pattern, "colour", text)
print(text2)

text3 = re.sub(pattern, "colour", text, count=1)
print(text3) # count number will make change according to the order