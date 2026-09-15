import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 14500, 13800, 16000, 17500, 19000],
    "Customers": [120, 145, 138, 160, 175, 190],
    "Profit": [3000, 3800, 3400, 4200, 4700, 5200]
})

print(data)

fig, ax = plt.subplots(2, 2, figsize=(10, 7))

ax[0, 0].plot(data["Month"], data["Sales"])
ax[0, 0].set_title("Monthly Sales")
ax[0, 0].set_xlabel("Month")
ax[0, 0].set_ylabel("Sales")
ax[0, 0].grid()

ax[0, 1].bar(data["Month"], data["Customers"])
ax[0, 1].set_title("Monthly Customers")
ax[0, 1].set_xlabel("Month")
ax[0, 1].set_ylabel("Customers")
ax[0, 1].grid(axis="y")

ax[1, 0].plot(data["Month"], data["Profit"])
ax[1, 0].set_title("Monthly Profit")
ax[1, 0].set_xlabel("Month")
ax[1, 0].set_ylabel("Profit")
ax[1, 0].grid()

ax[1, 1].scatter(data["Customers"], data["Profit"], s=100, alpha=0.7)
ax[1, 1].set_title("Customers vs Profit")
ax[1, 1].set_xlabel("Customers")
ax[1, 1].set_ylabel("Profit")
ax[1, 1].grid()

plt.tight_layout()
plt.savefig("business_dashboard.png")
plt.show()