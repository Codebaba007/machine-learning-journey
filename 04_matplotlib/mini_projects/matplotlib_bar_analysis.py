import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Headphones"],
    "Sales": [35, 50, 28, 65]
})

print(data)

plt.figure(figsize=(8, 5))

plt.bar(data["Product"], data["Sales"])

plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Units Sold")

plt.grid(axis="y")

plt.savefig("product_sales.png")
plt.show()