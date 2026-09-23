import pandas as pd

data = pd.DataFrame({
    "Student": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Henry", "Ivy", "Jack",
        "Kevin", "Liam"
    ],
    "Score": [45, 52, 60, 65, 68, 70, 72, 78, 85, 90, 95, 100]
})

scores = data["Score"]

q1 = scores.quantile(0.25)
q2 = scores.quantile(0.50)
q3 = scores.quantile(0.75)

iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = data[
    (scores < lower_bound) |
    (scores > upper_bound)
]

print("Q1:", q1)
print("Median:", q2)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print("\nPotential Outliers:")
print(outliers)