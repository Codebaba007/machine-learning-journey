student = {
    "name": "Mehedi",
    "age" : 23,
    "department" : "CSE",
    "University" : "UITS",
    "cgpa" : 3.52
}
print(student["name"])
print(student["age"])
print(student["department"])
print(student["University"])
print(student["cgpa"])

student["age"] = 24
student["section"] = "B"
student = {
    "name": "Mehedi",
    "age": 23,
    "department": "CSE"
}

key = input("Enter a key: ")

if key in student:
    print("Key exists.")
else:
    print("Key does not exist.")

student = {
    "name": "Mehedi",
    "age": 23,
    "department": "CSE",
    "cgpa": 3.52
}

for key, value in student.items():
    print(key, ":", value)
marks = {
    "Python": 85,
    "Mathematics": 78,
    "Statistics": 91,
    "Machine Learning": 88
}

total = 0

for mark in marks.values():
    total = total + mark

print("Total Marks =", total)

marks = {
    "Python": 85,
    "Mathematics": 78,
    "Statistics": 91,
    "Machine Learning": 88
}

highest = 0

for mark in marks.values():
    if mark > highest:
        highest = mark

print("Highest Mark =", highest)