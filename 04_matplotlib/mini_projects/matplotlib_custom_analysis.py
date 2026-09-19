import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 14500, 13800, 16000, 17500, 19000],
    "Customers": [120, 145, 138, 160, 175, 190]
})

print(data)

plt.figure(figsize=(9, 5))

plt.plot(
    data["Month"],
    data["Sales"],
    color="blue",
    marker="o",
    linestyle="--",
    linewidth=2,
    markersize=8,
    label="Sales"
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid()

plt.savefig("custom_sales_analysis.png")
plt.show()