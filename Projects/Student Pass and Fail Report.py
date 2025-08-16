# This project is done with map and filter function

students = [
    { "name" : "Athika", "marks" : 77 },
    { "name" : "Rittika", "marks" : 80 },
    { "name" : "Nabil", "marks" : 22 },
    {"name": "David", "marks": 29},
    {"name": "Eva", "marks": 91}
]

passed_students = filter(lambda s : s["marks"] > 40, students)
failed_students = filter(lambda s : s["marks"] < 40, students)

passed_message = map(lambda s : f"{s["name"]} passed with {s["marks"]} marks", passed_students)
failed_message = map(lambda s : f"{s["name"]} failed with {s["marks"]} marks", failed_students)

print("Passed Students:")
for msg in passed_message:
    print(msg)

print("Failed Students:")
for msg in failed_message:
    print(msg)