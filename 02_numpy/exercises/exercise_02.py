import numpy as np


students = np.array([
    [78, 85, 92],
    [67, 88, 95],
    [72, 81, 89],
    [90, 76, 84]
])

print(students.shape)

print(students.ndim)

print(students[0,0])

print(students[1,2])

print(students[:,0])

print(students[2:4])

