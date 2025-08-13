# dictionary is a data structure for python

studentId = {
    "101" : "Athika", # can use as string
    "102" : "Priya",
    103 : "Amanda", # can use as integer
    104 : "Lina",
}

print(studentId["101"])
print(studentId.get(103))
print(studentId.get("102", "not a valid key")) # will show 102 name as it present, not the value

print(studentId.get("106")) # will show none, as there's no 106
print(studentId.get("107", "not a valid key")) # will get default value, as there's no 107