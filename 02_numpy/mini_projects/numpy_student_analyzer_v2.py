import numpy as np


# Student marks
# Columns: Python, NumPy, Mathematics

marks = np.array([
    [78, 85, 92],
    [67, 88, 95],
    [72, 81, 89],
    [90, 76, 84],
    [85, 91, 87]
])


print("Student Marks")
print("====================")
print(marks)


# Shape and dimensions

print("\nArray Shape")
print("====================")
print(marks.shape)

print("\nNumber of Dimensions")
print("====================")
print(marks.ndim)


# First student's marks

print("\nFirst Student")
print("====================")
print(marks[0])


# First subject marks

print("\nPython Marks")
print("====================")
print(marks[:, 0])


# Last two students

print("\nLast Two Students")
print("====================")
print(marks[3:5])


# Update a mark

marks[0, 0] = 82

print("\nUpdated Marks")
print("====================")
print(marks)


# Add bonus marks

bonus_marks = marks + 5

print("\nMarks After Bonus")
print("====================")
print(bonus_marks)