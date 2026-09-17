import matplotlib.pyplot as plt

categories = ["Food", "Transport", "Entertainment", "Savings"]
amounts = [4000, 2000, 1500, 2500]

plt.figure(figsize=(7, 7))

plt.pie(
    amounts,
    labels=categories,
    autopct="%1.0f%%",
    startangle=90
)

plt.title("Monthly Budget Distribution")
plt.axis("equal")

plt.show()