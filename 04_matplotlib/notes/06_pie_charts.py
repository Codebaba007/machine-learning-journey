import matplotlib.pyplot as plt

categories = ["Rent", "Food", "Transport", "Other"]
expenses = [5000, 3000, 1500, 500]

plt.figure(figsize=(8, 8))

plt.pie(
    expenses,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90,
    explode=(0, 0.1, 0, 0),
    shadow=True
)
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Monthly Expenses")

plt.show()