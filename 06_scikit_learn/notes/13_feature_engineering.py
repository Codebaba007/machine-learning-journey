
import numpy as np
import pandas as pd

from sklearn.preprocessing import PolynomialFeatures

# -----------------------------------
# 1. Creating new features
# -----------------------------------

data = pd.DataFrame({
    "area": [1000, 1500, 2000],
    "price": [100000, 180000, 240000]
})

data["price_per_sqft"] = data["price"] / data["area"]

print("New feature: Price per square foot")
print(data)

# -----------------------------------
# 2. Creating total spending
# -----------------------------------

customers = pd.DataFrame({
    "monthly_spending": [500, 800, 300],
    "months_subscribed": [12, 6, 24]
})

customers["total_spending"] = (
    customers["monthly_spending"]
    * customers["months_subscribed"]
)

print("\nCustomer spending:")
print(customers)

# -----------------------------------
# 3. Log transformation
# -----------------------------------

income = np.array([20000, 25000, 30000, 50000, 500000])

log_income = np.log1p(income)

print("\nOriginal income:")
print(income)

print("\nLog-transformed income:")
print(log_income)

# -----------------------------------
# 4. Polynomial features
# -----------------------------------

X = [[2], [3], [4]]

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

print("\nOriginal features:")
print(X)

print("\nPolynomial features:")
print(X_poly)

print("\nFeature names:")
print(poly.get_feature_names_out(["x"]))

# -----------------------------------
# 5. Extracting date features
# -----------------------------------

dates = pd.DataFrame({
    "order_date": [
        "2026-01-05",
        "2026-02-14",
        "2026-03-20"
    ]
})

dates["order_date"] = pd.to_datetime(dates["order_date"])

dates["year"] = dates["order_date"].dt.year
dates["month"] = dates["order_date"].dt.month
dates["day"] = dates["order_date"].dt.day
dates["weekday"] = dates["order_date"].dt.dayofweek

print("\nDate features:")
print(dates)
