'''import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12000, 14500, 13800, 16000, 19000, 22000]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.annotate(
    "Highest Sales",
    xy=("Jun", 22000),
    xytext=("Apr", 23000),
    arrowprops=dict(arrowstyle="->")
)

plt.show()
import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]
scores = [45, 50, 58, 65, 72, 80]

plt.scatter(hours, scores)

plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")

plt.annotate(
    "Highest Score",
    xy=(6, 80),
    xytext=(4, 85),
    arrowprops=dict(arrowstyle="->")
)

plt.grid()
plt.show()'''
import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Tablet", "Headphones"]
sales = [35, 50, 28, 65]

plt.bar(products, sales)

plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Units Sold")

plt.annotate(
    "Highest Sales",
    xy=("Headphones", 65),
    xytext=(-70, 30),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->")
)

plt.grid(axis="y")
plt.show()