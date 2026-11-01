
import numpy as np
import pandas as pd

from sklearn.preprocessing import PolynomialFeatures

# -----------------------------------
# 1. Create a price per square foot feature
# -----------------------------------

houses = pd.DataFrame({
    "area": [1000, 1500, 2000, 2500],
    "price": [100000, 180000, 240000, 300000]
})

houses["price_per_sqft"] = houses["price"] / houses["area"]

print("House features:")
print(houses)

# -----------------------------------
# 2. Create total spending
# -----------------------------------

customers = pd.DataFrame({
    "monthly_spending": [500, 800, 300, 1000],
    "months_subscribed": [12, 6, 24, 10]
})

customers["total_spending"] = (
    customers["monthly_spending"]
    * customers["months_subscribed"]
)

print("\nCustomer features:")
print(customers)

# -----------------------------------
# 3. Log transformation
# -----------------------------------

income = np.array([20000, 30000, 50000, 500000])

log_income = np.log1p(income)

print("\nOriginal income:")
print(income)

print("\nLog-transformed income:")
print(log_income)

# -----------------------------------
# 4. Polynomial features
# -----------------------------------

X = [[2], [3], [4], [5]]

poly = PolynomialFeatures(degree=2)

X_poly = poly.fit_transform(X)

print("\nOriginal features:")
print(X)

print("\nPolynomial features:")
print(X_poly)

print("\nFeature names:")
print(poly.get_feature_names_out(["x"]))

# -----------------------------------
# 5. Extract date features
# -----------------------------------

orders = pd.DataFrame({
    "order_date": [
        "2026-01-05",
        "2026-02-14",
        "2026-03-20",
        "2026-04-10"
    ]
})

orders["order_date"] = pd.to_datetime(orders["order_date"])

orders["month"] = orders["order_date"].dt.month
orders["weekday"] = orders["order_date"].dt.dayofweek

print("\nDate features:")
print(orders)
