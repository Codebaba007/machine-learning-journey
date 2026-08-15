import numpy as np


marks = np.array([78, 85, 92, 67, 88, 95, 45, 73, 81, 90])


print("Student Marks")
print("====================")
print(marks)

print("\nStatistics")
print("====================")

print("Total:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))

passed = marks[marks >= 50]
failed = marks[marks < 50]

print("\nPassed Students")
print("====================")
print(passed)

print("\nFailed Students")
print("====================")
print(failed)

print("\nSorted Marks")
print("====================")
print(np.sort(marks))