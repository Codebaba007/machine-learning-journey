python_students = {
    "Mehedi",
    "Hasan",
    "Rahim",
    "Sakib"
}

ml_students = {
    "Mehedi",
    "Rahim",
    "Karim"
}
all_students = python_students | ml_students
both_courses = python_students & ml_students
python_only = python_students - ml_students

print("========================================")
print("       Student Set Analyzer")
print("========================================")

print()
print("All Students:")

for student in all_students:
    print(student)

print()
print("Students Taking Both:")

for student in both_courses:
    print(student)

print()
print("Python Only:")

for student in python_only:
    print(student)

print()
print("Total Unique Students:", len(all_students))

print()
print("========================================")