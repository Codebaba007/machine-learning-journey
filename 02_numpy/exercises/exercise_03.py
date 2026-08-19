import numpy as np


marks = np.array([
    [78, 85, 92],
    [67, 88, 95],
    [72, 81, 89],
    [90, 76, 84],
    [85, 91, 87]
])


# Exercise 1 — Basic Aggregation

print("Total:", np.sum(marks))
print("Overall Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))


# Exercise 2 — Subject Analysis

print("\nSubject Analysis")
print("====================")

print("Subject Totals:", np.sum(marks, axis=0))
print("Subject Averages:", np.mean(marks, axis=0))
print("Subject Highest:", np.max(marks, axis=0))
print("Subject Lowest:", np.min(marks, axis=0))


# Exercise 3 — Student Analysis

print("\nStudent Analysis")
print("====================")

print("Student Totals:", np.sum(marks, axis=1))
print("Student Averages:", np.mean(marks, axis=1))
print("Student Highest:", np.max(marks, axis=1))
print("Student Lowest:", np.min(marks, axis=1))


# Exercise 4 — Standard Deviation

print("\nStandard Deviation")
print("====================")

print("Overall:", np.std(marks))
print("By Subject:", np.std(marks, axis=0))
print("By Student:", np.std(marks, axis=1))


# Exercise 5 — Median

print("\nMedian")
print("====================")

print("Overall:", np.median(marks))
print("By Subject:", np.median(marks, axis=0))
print("By Student:", np.median(marks, axis=1))


# Exercise 6 — Maximum and Minimum Positions

print("\nMaximum and Minimum Positions")
print("====================")

print("Overall Maximum Position:", np.argmax(marks))
print("Overall Minimum Position:", np.argmin(marks))

print("Maximum Position by Subject:", np.argmax(marks, axis=0))
print("Minimum Position by Subject:", np.argmin(marks, axis=0))


# Exercise 7 — Range

print("\nRange")
print("====================")

print("Overall Range:", np.ptp(marks))
print("Range by Subject:", np.ptp(marks, axis=0))
print("Range by Student:", np.ptp(marks, axis=1))


# Exercise 8 — Boolean Analysis

print("\nBoolean Analysis")
print("====================")

print("At least one mark >= 90:", np.any(marks >= 90))
print("All marks >= 50:", np.all(marks >= 50))
print("At least one mark < 50:", np.any(marks < 50))
print("All marks >= 70:", np.all(marks >= 70))


# Exercise 9 — Count Values

print("\nCount Values")
print("====================")

print("Marks >= 80:", np.sum(marks >= 80))
print("Marks >= 90:", np.sum(marks >= 90))
print("Marks < 70:", np.sum(marks < 70))
print(
    "Marks between 70 and 90:",
    np.sum((marks >= 70) & (marks <= 90))
)


# Exercise 10 — Subject-Level Boolean Analysis

print("\nSubject-Level Boolean Analysis")
print("====================")

print(
    "At least one mark >= 90:",
    np.any(marks >= 90, axis=0)
)

print(
    "All students >= 70:",
    np.all(marks >= 70, axis=0)
)

print(
    "Students scoring >= 80:",
    np.sum(marks >= 80, axis=0)
)


# Challenge — Student Performance Summary

print("\nStudent Performance Summary")
print("====================")

totals = np.sum(marks, axis=1)
averages = np.mean(marks, axis=1)
highest = np.max(marks, axis=1)
lowest = np.min(marks, axis=1)
ranges = np.ptp(marks, axis=1)
standard_deviations = np.std(marks, axis=1)


for i in range(len(marks)):
    print(f"\nStudent {i + 1}")
    print("Total:", totals[i])
    print("Average:", averages[i])
    print("Highest:", highest[i])
    print("Lowest:", lowest[i])
    print("Range:", ranges[i])
    print("Standard Deviation:", standard_deviations[i])