import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Student": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Henry", "Ivy", "Jack",
        "Kevin", "Liam", "Mia", "Noah", "Olivia",
        "Paul", "Quinn", "Ryan", "Sophia", "Tom"
    ],
    "Score": [
        45, 52, 58, 61, 64,
        66, 68, 70, 71, 73,
        75, 76, 78, 80, 82,
        85, 87, 90, 94, 100
    ]
})

scores = data["Score"]

mean = scores.mean()
median = scores.median()
std = scores.std()
q1 = scores.quantile(0.25)
q3 = scores.quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = data[
    (scores < lower_bound) |
    (scores > upper_bound)
]

print("Student Score Distribution Analysis")
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print("\nPotential Outliers:")
print(outliers)

if mean > median:
    print("\nDistribution: Right-skewed")
elif mean < median:
    print("\nDistribution: Left-skewed")
else:
    print("\nDistribution: Approximately symmetric")

plt.hist(scores, bins=6)
plt.title("Student Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.grid()
plt.show()