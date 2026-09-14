import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Size_sqft": [800, 1000, 1200, 1400, 1600, 1800, 2000, 2200],
    "Price": [35, 42, 50, 58, 65, 73, 82, 91]
})

print(data)

plt.figure(figsize=(8, 5))
plt.scatter(
    data["Size_sqft"],
    data["Price"],
    s=100,
    alpha=0.7
)

plt.title("House Size vs House Price")
plt.xlabel("House Size (sqft)")
plt.ylabel("Price (Lakhs)")
plt.grid()

plt.savefig("house_price_analysis.png")
plt.show()