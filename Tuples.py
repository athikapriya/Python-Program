# Typles is a kind of data structure as list
# but list values can be changed, but tuples values are not
# It's better to use first bracket for tuples, whereas list uses third bracket, dictionaries uses second bracket

students = (
    "Athika",
    ("Priya", 28, 4.00), # tuples can take tuples
    "Lina"
)

print(students)
print(students[0])
print(students[1]) # print all values of index 1
print(students[1][1])
print(students[1:]) # print all values starting from index 1
