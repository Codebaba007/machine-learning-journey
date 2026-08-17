'''import numpy as np

marks = np.array([
    [78, 85, 92],
    [67, 88, 95]
])

print(marks)
print(marks.shape)

marks2 = np.array([
    [78, 85, 92],
    [67, 88, 95]
])

print(marks2.ndim)

a = np.array([1, 2, 3])

b = np.array([
    [1, 2],
    [3, 4]
])

print(a.ndim)
print(b.ndim)'''
# NumPy Day 2 — Array Operations and Data Manipulation

import numpy as np


# ==========================================
# 1. Array Shape
# ==========================================

marks = np.array([78, 85, 92, 67, 88])

print("Marks:")
print(marks)

print("\nShape:")
print(marks.shape)


# ==========================================
# 2. Two-Dimensional Arrays
# ==========================================

students = np.array([
    [78, 85, 92],
    [67, 88, 95],
    [72, 81, 89],
    [90, 76, 84]
])

print("\nStudents:")
print(students)

print("\nShape:")
print(students.shape)

print("\nNumber of Dimensions:")
print(students.ndim)


# ==========================================
# 3. 2D Indexing
# ==========================================

print("\nFirst Row, Second Column:")
print(students[0, 1])

print("\nSecond Row, Third Column:")
print(students[1, 2])

numbers = np.array([1, 2, 3, 4, 5, 6])

print(numbers.reshape(2, -1))
# ==========================================
# 11. Broadcasting
# ==========================================

markaaa = np.array([60, 70, 80, 90])

print("\nBroadcasting:")
print(markaaa + 5)


markaaa = np.array([
    [60, 70, 80],
    [75, 85, 95]
])

print("\n2D Broadcasting:")
print(markaaa + 5)


bonus = np.array([5, 10, 15])

print("\nBroadcasting with Two Arrays:")
print(markaaa + bonus)

zeros = np.zeros(5)

print(zeros)

zeros2d = np.zeros((2, 3))

print(zeros2d)

ones = np.ones(5)

print(ones)
onesd = np.ones((3, 4))

print(onesd)