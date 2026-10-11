import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


data = pd.DataFrame({
    "area_sqft": [
        600, 700, 800, 900, 1000, 1100,
        1200, 1300, 1400, 1500, 1600, 1700,
        1800, 1900, 2000, 2100, 2200, 2300
    ],
    "price_lakh": [
        28, 32, 36, 39, 43, 47,
        51, 54, 59, 62, 66, 71,
        74, 79, 83, 86, 91, 95
    ]
})

X = data[["area_sqft"]]
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

results = pd.DataFrame({
    "Area (sq ft)": X_test["area_sqft"],
    "Actual Price (Lakh)": y_test,
    "Predicted Price (Lakh)": predictions
})

results["Residual"] = (
    results["Actual Price (Lakh)"]
    - results["Predicted Price (Lakh)"]
)

print("House Price Prediction Results")
print(results.round(2))

print("\nModel Coefficient:", round(model.coef_[0], 4))
print("Model Intercept:", round(model.intercept_, 4))

mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:", round(mae, 2), "lakh")

new_house = pd.DataFrame({
    "area_sqft": [1500]
})

predicted_price = model.predict(new_house)

print(
    "\nPredicted price for a 1500 sq ft house:",
    round(predicted_price[0], 2),
    "lakh"
)


# Plot the training data and fitted regression line

plt.figure(figsize=(8, 5))

plt.scatter(
    X_train["area_sqft"],
    y_train,
    label="Training data"
)

line_areas = pd.DataFrame({
    "area_sqft": sorted(X_train["area_sqft"])
})

line_predictions = model.predict(line_areas)

plt.plot(
    line_areas["area_sqft"],
    line_predictions,
    label="Regression line"
)

plt.xlabel("House Area (sq ft)")
plt.ylabel("Price (Lakh)")
plt.title("Linear Regression: House Price Prediction")
plt.legend()

plt.tight_layout()
plt.show()


# Compare actual and predicted test prices

plt.figure(figsize=(7, 5))

plt.scatter(
    y_test,
    predictions
)

lower = min(y_test.min(), predictions.min())
upper = max(y_test.max(), predictions.max())

plt.plot(
    [lower, upper],
    [lower, upper],
    linestyle="--"
)

plt.xlabel("Actual Price (Lakh)")
plt.ylabel("Predicted Price (Lakh)")
plt.title("Actual vs Predicted Prices")

plt.tight_layout()
plt.show()