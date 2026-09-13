import matplotlib.pyplot as plt
'''
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
scores = [85, 78, 92, 88, 76]
plt.bar(students, scores)
plt.title("Student Score Comparison")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.grid(axis="y")
plt.figure(figsize=(8, 5))
plt.show()
'''
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
scores = [85, 78, 92, 88, 76]
plt.barh(students, scores)
plt.title("Student Score Comparison")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.grid(axis="y")
plt.figure(figsize=(8, 5))
plt.show()