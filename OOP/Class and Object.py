class Student :
    roll = ""
    gpa = ""

rahim= Student()
print(isinstance(rahim, Student))
rahim.roll= 11
rahim.gpa = "A"
print(f"Name : Rahim, Roll : {rahim.roll}, GPA : {rahim.gpa}")