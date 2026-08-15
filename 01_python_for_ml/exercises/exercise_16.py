import numpy as np

marks = np.array([78, 85, 92, 67, 88, 95])
bonus = marks + 5
doubled = marks * 2
passed = marks >= 50
print("Passed:", passed)
print("Marks:", marks)
print("After bonus: ", bonus)
print("Doubled: ",doubled)
print("First mark:", marks[0])
print("Last mark:", marks[-1])
print("Number of marks:", len(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Total:", np.sum(marks))
print("Sorted:", np.sort(marks))
print("Above 80:", marks[marks > 80])