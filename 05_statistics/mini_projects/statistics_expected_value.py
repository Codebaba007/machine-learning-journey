import pandas as pd
import numpy as np

data = pd.DataFrame({
    "Daily Sales": [1000, 2000, 3000, 4000],
    "Probability": [0.2, 0.4, 0.3, 0.1]
})

data["Weighted Sales"] = (
    data["Daily Sales"] * data["Probability"]
)

expected_sales = data["Weighted Sales"].sum()

print("Daily Sales Probability Analysis")
print(data)

print("\nProbability Sum:", data["Probability"].sum())
print("Expected Daily Sales:", expected_sales)