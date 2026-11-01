
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

# -----------------------------------
# 1. Create dataset
# -----------------------------------

data = pd.DataFrame({
    "area": [
        900, 1000, 1100, 1200,
        1300, 1400, 1500, 1600,
        1700, 1800, 1900, 2000,
        2100, 2200, 2300, 2400
    ],
    "bedrooms": [
        2, 2, 2, 2,
        3, 3, 3, 3,
        3, 3, 4, 4,
        4, 4, 4, 5
    ],
    "age": [
        15, 12, 10, 9,
        8, 7, 6, 5,
        5, 4, 4, 3,
        3, 2, 2, 1
    ],
    "price": [
        100, 110, 120, 130,
        145, 155, 165, 175,
        185, 195, 215, 230,
        240, 255, 270, 300
    ]
})

# -----------------------------------
# 2. Feature engineering
# -----------------------------------

data["price_per_sqft"] = (
    data["price"] / data["area"]
)

print("Dataset with engineered feature:")
print(data.head())

# -----------------------------------
# 3. Select features and target
# -----------------------------------

X = data[[
    "area",
    "bedrooms",
    "age",
    "price_per_sqft"
]]

y = data["price"]

# -----------------------------------
# 4. Split data
# -----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# -----------------------------------
# 5. Build ML pipeline
# -----------------------------------

model = Pipeline([
    ("polynomial", PolynomialFeatures(
        degree=2,
        include_bias=False
    )),
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression())
])

# -----------------------------------
# 6. Train model
# -----------------------------------

model.fit(X_train, y_train)

# -----------------------------------
# 7. Make predictions
# -----------------------------------

predictions = model.predict(X_test)

print("\nActual prices:")
print(y_test.to_numpy())

print("\nPredicted prices:")
print(np.round(predictions, 2))

# -----------------------------------
# 8. Evaluate model
# -----------------------------------

mae = mean_absolute_error(y_test, predictions)

print(f"\nMean Absolute Error: {mae:.2f}")

# -----------------------------------
# 9. Predict a new house
# -----------------------------------

new_house = pd.DataFrame({
    "area": [1800],
    "bedrooms": [3],
    "age": [5],
    "price_per_sqft": [0.11]
})

new_prediction = model.predict(new_house)

print("\nPredicted price for new house:")
print(f"{new_prediction[0]:.2f}")
