import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Student": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Henry", "Ivy", "Jack",
        "Kevin", "Liam", "Mia", "Noah", "Olivia"
    ],
    "Score": [
        45, 52, 58, 60, 62,
        65, 67, 68, 70, 72,
        74, 76, 80, 85, 90
    ]
})

print(data)

plt.figure(figsize=(8, 5))
plt.hist(data["Score"], bins=5, edgecolor="black")

plt.title("Student Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.grid(axis="y")

plt.savefig("student_score_distribution.png")
plt.show()