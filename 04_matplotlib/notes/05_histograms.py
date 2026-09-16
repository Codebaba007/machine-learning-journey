'''import matplotlib.pyplot as plt

scores = [
    45, 52, 55, 58, 60,
    61, 62, 64, 65, 67,
    68, 70, 71, 72, 74,
    75, 78, 80, 85, 90
]
plt.hist(scores, bins=10, edgecolor='black', alpha=0.7)

plt.title("Distribution of Scores")
plt.xlabel("Scores")
plt.ylabel("Number of Students")
plt.yticks(range(0, 4))
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Student": ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry"],
    "Score": [55, 62, 68, 72, 75, 78, 85, 90]
})

print("Student Data")
print(data)

plt.figure(figsize=(8, 5))

plt.hist(
    data["Score"],
    bins=5,
    edgecolor="black"

)

plt.title("Student Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.grid(axis="y")

plt.show()'''

import matplotlib.pyplot as plt

class_a = [55, 60, 62, 65, 68, 70, 72, 75, 78, 80]
class_b = [60, 65, 68, 70, 72, 75, 78, 82, 85, 90]

plt.hist(class_a, bins=5, alpha=0.5, label="Class A")
plt.hist(class_b, bins=5, alpha=0.5, label="Class B")

plt.title("Exam Score Distributions")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.legend()

plt.show()