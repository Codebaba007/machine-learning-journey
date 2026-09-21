import pandas as pd

data = pd.DataFrame({
    "Student": [
        "Alice", "Bob", "Charlie", "David", "Emma",
        "Frank", "Grace", "Henry", "Ivy", "Jack"
    ],
    "Score": [45, 52, 60, 65, 68, 70, 72, 75, 80, 90]
})

print("Student Score Data")
print(data)

print("\nDescriptive Statistics")

print("Mean:", data["Score"].mean())
print("Median:", data["Score"].median())
print("Mode:", data["Score"].mode().tolist())
print("Minimum:", data["Score"].min())
print("Maximum:", data["Score"].max())
print("Range:", data["Score"].max() - data["Score"].min())