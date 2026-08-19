import numpy as np

marks = np.array([
    [78, 85, 92],
    [67, 88, 95],
    [72, 81, 89],
    [90, 76, 84]
])

print(np.max(marks, axis=0))
print(np.max(marks, axis=1))
print(np.min(marks, axis=0))
print(np.min(marks, axis=1))
print("\n")
print(np.std(marks))

numbers = np.array([10, 20, 30, 40, 50])

print(np.median(numbers))

numbers = np.array([10, 20, 30, 40])

print(np.median(numbers))
print("Subject Totals:", np.sum(marks, axis=0))
print("Subject Averages:", np.mean(marks, axis=0))
print("Subject Highest:", np.max(marks, axis=0))
print("Subject Lowest:", np.min(marks, axis=0))
print("Subject Median:", np.median(marks, axis=0))
print("Subject Standard Deviation:", np.std(marks, axis=0))
print("Subject Range:", np.ptp(marks, axis=0))
marks = np.array([78, 85, 92, 67, 88, 95, 72])

print(marks >= 80)
print(np.all(marks >= 70, axis=0))