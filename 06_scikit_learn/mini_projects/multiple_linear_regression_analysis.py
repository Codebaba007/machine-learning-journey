import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


data = pd.DataFrame({
    "area_sqft": [
        650, 700, 750, 800, 850, 900, 950, 1000,
        1050, 1100, 1150, 1200, 1250, 1300, 1350,
        1400, 1450, 1500, 1550, 1600, 1650, 1700,
        1750, 1800, 1850, 1900, 1950, 2000, 2100, 2200
    ],
    "bedrooms": [
        1, 1, 1, 2, 2, 2, 2, 2,
        2, 2, 3, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 4,
        4, 4, 4, 4, 4, 4, 4, 5
    ],
    "price_lakh": [
        28, 30, 32, 35, 37, 40, 43, 45,
        48, 50, 54, 57, 60, 63, 66,
        68, 71, 74, 77, 79, 82, 86,
        89, 92, 94, 97, 100, 103, 108, 115
    ]
})

X = data[["area_sqft", "bedrooms"]]
y = data["price_lakh"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

results = X_test.copy()
results["Actual Price"] = y_test
results["Predicted Price"] = predictions
results["Residual"] = y_test - predictions

print("House Price Prediction Results")
print(results.round(2))

print("\nModel Intercept:", round(model.intercept_, 4))

print("\nModel Coefficients")
for feature, coefficient in zip(X.columns, model.coef_):
    print(f"{feature}: {coefficient:.4f}")

mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:", round(mae, 2), "lakh")


new_house = pd.DataFrame({
    "area_sqft": [1600],
    "bedrooms": [3]
})

predicted_price = model.predict(new_house)

print("\nNew House Prediction")
print("Area: 1600 sq ft")
print("Bedrooms: 3")
print("Predicted price:", round(predicted_price[0], 2), "lakh")


plt.figure(figsize=(7, 5))

plt.scatter(y_test, predictions)

lower = min(y_test.min(), predictions.min())
upper = max(y_test.max(), predictions.max())

plt.plot(
    [lower, upper],
    [lower, upper],
    linestyle="--"
)

plt.xlabel("Actual Price (Lakh)")
plt.ylabel("Predicted Price (Lakh)")
plt.title("Multiple Linear Regression: Actual vs Predicted")
plt.tight_layout()
plt.show()