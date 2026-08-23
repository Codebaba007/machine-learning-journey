import pandas as pd

students = pd.DataFrame({
    "Student" : ["A", "B", "C", "D", "E"],
    "Python" : [90, 80, 70, 60, 50],
    "Numpy" : [85, 75, 65, 55, 45],
    "Math" : [95, 85, 75, 65, 55]
})
print("\nStudent Data: \n", students)
print("\n")
print("\nFirst Student: \n", students.loc[0])

print("\nFirst Three Students: \n", students.loc[0:2])

print("\nSelected Data: \n", students.loc[0:2, ["Student", "Python"]])
print("\nUsing iloc")
print("====================")
print(students.iloc[0])

print("\nSpecific Positions")
print("====================")
print(students.iloc[0:3, 1:3])

print("\nPython Marks >= 80")
print("====================")
print(students[students["Python"] >= 80])


# 7. Multiple Conditions — AND

print("\nPython >= 80 AND Math >= 90")
print("====================")

filtered = students[
    (students["Python"] >= 80) &
    (students["Math"] >= 90)
]

print(filtered)


# 8. Multiple Conditions — OR

print("\nPython >= 90 OR Math >= 90")
print("====================")

filtered = students[
    (students["Python"] >= 90) |
    (students["Math"] >= 90)
]

print(filtered)


# 9. Filtering a Range

print("\nPython Between 70 and 85")
print("====================")

filtered = students[
    (students["Python"] >= 70) &
    (students["Python"] <= 85)
]

print(filtered)


# 10. Selecting a Column From Filtered Data

print("\nStudents With Python >= 80")
print("====================")

filtered = students[students["Python"] >= 80]

print(filtered["Student"])