import matplotlib.pyplot as plt
'''
scores = [
    45, 52, 55, 58, 60,
    61, 62, 64, 65, 67,
    68, 70, 71, 72, 74,
    75, 78, 80, 85, 90
]

plt.figure(figsize=(8, 6))

plt.boxplot(scores)

plt.title("Exam Score Distribution")
plt.ylabel("Scores")
plt.show()

import matplotlib.pyplot as plt

scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 200]

plt.boxplot(scores)

plt.title("Score Distribution")
plt.ylabel("Score")

plt.show()

class_a = [55, 60, 65, 70, 75]
class_b = [60, 65, 70, 75, 80]
class_c = [50, 58, 63, 68, 72]

plt.boxplot([class_a, class_b, class_c])

plt.xticks(
    [1, 2, 3],
    ["Class A", "Class B", "Class C"]
)

plt.ylabel("Score")
plt.title("Class Score Comparison")

plt.show()'''
import pandas as pd


data = pd.DataFrame({
    "Class": [
        "A", "A", "A", "A", "A",
        "B", "B", "B", "B", "B"
    ],
    "Score": [
        55, 60, 65, 70, 80,
        60, 68, 72, 78, 90
    ]
})

class_a = data[data["Class"] == "A"]["Score"]
class_b = data[data["Class"] == "B"]["Score"]

plt.figure(figsize=(7, 5))

plt.boxplot([class_a, class_b])

plt.title("Class Score Distribution")
plt.ylabel("Score")
plt.xticks([1, 2], ["Class A", "Class B"])

plt.show()