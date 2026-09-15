import matplotlib.pyplot as plt
'''
days = [1, 2, 3, 4, 5]
scores = [60, 65, 72, 80, 88]

products = ["A", "B", "C", "D"]
sales = [20, 35, 30, 45]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(days, scores)
plt.title("Learning Progress")
plt.xlabel("Day")
plt.ylabel("Score")
plt.grid()

plt.subplot(1, 2, 2)
plt.bar(products, sales)
plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.grid(axis="y")

plt.tight_layout()
plt.show()'''

days = [1, 2, 3, 4, 5]
scores = [60, 65, 72, 80, 88]

products = ["A", "B", "C", "D"]
sales = [20, 35, 30, 45]

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].plot(days, scores)
ax[0].set_title("Learning Progress")
ax[0].set_xlabel("Day")
ax[0].set_ylabel("Score")
ax[0].grid()

ax[1].bar(products, sales)
ax[1].set_title("Product Sales")
ax[1].set_xlabel("Product")
ax[1].set_ylabel("Sales")
ax[1].grid(axis="y")

plt.tight_layout()
plt.show()