import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Category": ["Rent", "Food", "Transport", "Entertainment", "Savings"],
    "Amount": [12000, 5000, 2500, 1500, 4000]
})

print(data)

plt.figure(figsize=(8, 8))

plt.pie(
    data["Amount"],
    labels=data["Category"],
    autopct="%1.0f%%",
    startangle=90,
    explode=[0.05, 0, 0, 0, 0]
)

plt.title("Monthly Expense Distribution")
plt.axis("equal")

plt.savefig("expense_distribution.png")
plt.show()