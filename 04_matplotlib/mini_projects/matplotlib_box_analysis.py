import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Department": [
        "CSE", "CSE", "CSE", "CSE", "CSE",
        "EEE", "EEE", "EEE", "EEE", "EEE",
        "BBA", "BBA", "BBA", "BBA", "BBA"
    ],
    "Salary": [
        35000, 40000, 45000, 48000, 55000,
        30000, 35000, 38000, 42000, 47000,
        28000, 32000, 35000, 37000, 45000
    ]
})

print(data)

cse = data[data["Department"] == "CSE"]["Salary"]
eee = data[data["Department"] == "EEE"]["Salary"]
bba = data[data["Department"] == "BBA"]["Salary"]

plt.figure(figsize=(8, 5))

plt.boxplot([cse, eee, bba])

plt.title("Salary Distribution by Department")
plt.ylabel("Salary")
plt.xticks([1, 2, 3], ["CSE", "EEE", "BBA"])

plt.savefig("salary_distribution.png")
plt.show()