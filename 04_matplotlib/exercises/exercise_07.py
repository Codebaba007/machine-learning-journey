import matplotlib.pyplot as plt

class_a = [55, 60, 62, 65, 68, 70, 72, 75, 78, 80]
class_b = [60, 65, 68, 70, 72, 75, 78, 82, 85, 90]
class_c = [50, 55, 58, 63, 66, 69, 71, 73, 76, 79]

plt.figure(figsize=(8, 5))

plt.boxplot([class_a, class_b, class_c])

plt.title("Class Score Distribution")
plt.ylabel("Score")
plt.xticks([1, 2, 3], ["Class A", "Class B", "Class C"])

plt.show()