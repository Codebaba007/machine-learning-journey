student = {
    "name": "Mehedi",
    "age": 23,
    "department": "CSE"
}

print(student["department"])

student["age"] = 24
print(student["age"])

student = {
    "name": "Mehedi",
    "age": 23
}

student["cgpa"] = 3.52

print(len(student))

student = {
    "name": "Mehedi",
    "age": 23
}

print(student.get("email", "Not provided"))