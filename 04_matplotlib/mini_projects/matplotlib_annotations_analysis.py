import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 14500, 13800, 16000, 19000, 22000]
})

print(data)

plt.figure(figsize=(9, 5))

plt.plot(
    data["Month"],
    data["Sales"],
    marker="o",
    linewidth=2,
    label="Sales"
)

plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid()

plt.annotate(
    "Highest Sales",
    xy=("Jun", 22000),
    xytext=(-90, 30),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->")
)

plt.annotate(
    "Sales Drop",
    xy=("Mar", 13800),
    xytext=(-70, -45),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->")
)

plt.savefig("sales_annotations.png")
plt.show()