import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Score": [
        45, 50, 52, 55, 60, 62, 64, 65, 67, 70,
        72, 75, 80, 85, 90, 95, 100
    ]
})

scores = data["Score"]

print("Mean:", scores.mean())
print("Median:", scores.median())
print("Standard Deviation:", scores.std())
print("Q1:", scores.quantile(0.25))
print("Q3:", scores.quantile(0.75))

plt.hist(scores, bins=6)
plt.title("Student Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.show()