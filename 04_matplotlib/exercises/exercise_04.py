import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
scores = [55, 62, 70, 78, 85]

products = ["Laptop", "Phone", "Tablet", "Headphones"]
sales = [35, 50, 28, 65]

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].plot(days, scores)
ax[0].set_title("Learning Progress")
ax[0].set_xlabel("Day")
ax[0].set_ylabel("Score")
ax[0].grid()

ax[1].bar(products, sales)
ax[1].set_title("Product Sales")
ax[1].set_xlabel("Product")
ax[1].set_ylabel("Units Sold")
ax[1].grid(axis="y")

plt.tight_layout()
plt.show()