import pandas as pd


students = pd.DataFrame({
    "Student": [
        "Student 1",
        "Student 2",
        "Student 3",
        "Student 4",
        "Student 5",
        "Student 6",
        "Student 7",
        "Student 8",
        "Student 9",
        "Student 10"
    ],
    "Python": [78, 67, 72, 90, 85, 92, 74, 88, 81, 95],
    "NumPy": [85, 88, 81, 76, 91, 89, 79, 94, 84, 90],
    "Math": [92, 95, 89, 84, 87, 93, 82, 91, 86, 96]
})


print("STUDENT DATA FILTER")
print("============================")


# 1. Complete dataset

print("\nComplete Dataset")
print("----------------------------")
print(students)


# 2. First 3 students

print("\nFirst 3 Students")
print("----------------------------")
print(students.loc[0:2])


# 3. Last 2 students

print("\nLast 2 Students")
print("----------------------------")
print(students.iloc[-2:])


# 4. Student and Python columns

print("\nStudent and Python")
print("----------------------------")
print(students[["Student", "Python"]])


# 5. Python >= 80

print("\nPython >= 80")
print("----------------------------")
print(students[students["Python"] >= 80])


# 6. Math >= 90

print("\nMath >= 90")
print("----------------------------")
print(students[students["Math"] >= 90])


# 7. Python >= 80 AND NumPy >= 80

print("\nPython >= 80 AND NumPy >= 80")
print("----------------------------")

filtered = students[
    (students["Python"] >= 80) &
    (students["NumPy"] >= 80)
]

print(filtered)


# 8. Python >= 90 OR Math >= 90

print("\nPython >= 90 OR Math >= 90")
print("----------------------------")

filtered = students[
    (students["Python"] >= 90) |
    (students["Math"] >= 90)
]

print(filtered)


# 9. Python between 70 and 85

print("\nPython Between 70 and 85")
print("----------------------------")

filtered = students[
    (students["Python"] >= 70) &
    (students["Python"] <= 85)
]

print(filtered)


# 10. Students with average >= 80

students["Average"] = students[
    ["Python", "NumPy", "Math"]
].mean(axis=1)

print("\nStudents With Average >= 80")
print("----------------------------")

high_performers = students[students["Average"] >= 80]

print(high_performers[["Student", "Average"]])