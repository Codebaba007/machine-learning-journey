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


# Array information

print("\nArray Shape")
print("====================")
print(marks.shape)

print("\nNumber of Dimensions")
print("====================")
print(marks.ndim)


# First student

print("\nFirst Student")
print("====================")
print(marks[0])


# First subject

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


# Add the same bonus to every mark

bonus_marks = marks + 5

print("\nMarks After 5 Point Bonus")
print("====================")
print(bonus_marks)


# Broadcasting

subject_bonus = np.array([5, 10, 15])

broadcasted_marks = marks + subject_bonus

print("\nSubject-Specific Bonus")
print("====================")
print(broadcasted_marks)


# Create an array using arange

student_numbers = np.arange(1, 6)

print("\nStudent Numbers")
print("====================")
print(student_numbers)


# Create zeros and ones arrays

zeros = np.zeros((2, 3))
ones = np.ones((2, 3))

print("\nZeros Array")
print("====================")
print(zeros)

print("\nOnes Array")
print("====================")
print(ones)