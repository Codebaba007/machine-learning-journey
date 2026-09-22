import pandas as pd

data = pd.DataFrame({
    "Student": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Henry", "Ivy", "Jack"
    ],
    "Score": [45, 52, 60, 65, 68, 70, 72, 78, 85, 90]
})

print("Student Score Data")
print(data)

print("\nMean:", data["Score"].mean())
print("Variance:", data["Score"].var())
print("Standard Deviation:", data["Score"].std())

print("\nMinimum:", data["Score"].min())
print("Maximum:", data["Score"].max())
print("Range:", data["Score"].max() - data["Score"].min())