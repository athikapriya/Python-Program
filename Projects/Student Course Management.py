students = [
    ("Athika", 1 ),
    ("Rittika", 2 ),
]

course = { "Bangla", "English" }

marks = {
    1 : 80,
    2 : 70,
}

name = input("Enter student name : ")
roll = input("Enter roll no : ")
students.append((name, roll))
print("\n✅ Student added")

new_course = input("Enter new course name : ")
course.add(new_course)
print("\n✅ Course added")
new_marks = input("Enter new marks : ")
marks[roll] = new_marks
print("\n Marks added")

print("\n === Student Lists ===")
for s in students:
    print(f"Name : {s[0]}, Roll : {s[1]}")

print("\n === Course Lists ===")
for c in course:
    print(c)

print("\n === Marks Lists ===")
for roll_no, marks in marks.items():
    print(f"Roll No: {roll_no}, Marks: {marks}")
