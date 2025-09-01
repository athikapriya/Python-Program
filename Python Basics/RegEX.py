# Regular expressions are tools for manipulating strings
'''
Purpose
    verifying that strings match a pattern
    performing substitutions on s string
'''
'''
1. match() -> matches at the beginning of a string
2. search() -> finds a match of a pattern anywhere in the string
3. findall() -> returns a list of all substrings that match a pattern
'''

import re

pattern = r"color" # here r for row
if re.match(pattern,"Red is a color"):
    print("match")
elif re.search(pattern,"Red is a color"):
    print("search result found")
else:
    print("not matched")

print(re.findall(pattern,"Red is a color, I love red color."))

# --------------------
new_pattern = r"mango"
text = "mango is my favourite"

match = re.search(new_pattern,text)

if match:
    print(match.start())
    print(match.end())
    print(match.span()) # start and ending index