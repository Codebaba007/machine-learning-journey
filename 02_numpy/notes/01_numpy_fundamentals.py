import numpy as np

marks = np.array([85, 72, 91, 68, 95])

print(marks)
print(type(marks))

print("First mark:", marks[0])
print("Last mark:", marks[-1])

print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))