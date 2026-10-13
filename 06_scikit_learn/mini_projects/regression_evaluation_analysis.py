import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.dummy import DummyRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


data = pd.DataFrame({
    "area_sqft": [
        600, 650, 700, 750, 800, 850, 900, 950,
        1000, 1050, 1100, 1150, 1200, 1250, 1300,
        1350, 1400, 1450, 1500, 1550, 1600, 1650,
        1700, 1750, 1800, 1850, 1900, 1950, 2000, 2100
    ],
    "bedrooms": [
        1, 1, 1, 2, 2, 2, 2, 2,
        2, 2, 2, 3, 3, 3, 3,
        3, 3, 3, 3, 3, 3, 4,
        4, 4, 4, 4, 4, 4, 4, 5
    ],
    "price_lakh": [
        28, 30, 32, 35, 37, 40, 43, 45,
        48, 50, 53, 56, 59, 62, 65,
        68, 71, 74, 77, 80, 83, 86,
        89, 92, 95, 98, 101, 104, 108, 115
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


# Train the linear regression model

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)


# Create a mean-prediction baseline

baseline = DummyRegressor(strategy="mean")
baseline.fit(X_train, y_train)

baseline_predictions = baseline.predict(X_test)


# Calculate evaluation metrics

def evaluate_model(actual, predicted):
    mse = mean_squared_error(actual, predicted)

    return {
        "MAE": mean_absolute_error(actual, predicted),
        "MSE": mse,
        "RMSE": np.sqrt(mse),
        "R²": r2_score(actual, predicted)
    }


model_metrics = evaluate_model(y_test, predictions)
baseline_metrics = evaluate_model(y_test, baseline_predictions)

comparison = pd.DataFrame({
    "Linear Regression": model_metrics,
    "Mean Baseline": baseline_metrics
})

print("Model Evaluation")
print(comparison.round(3))


# Show actual and predicted test prices

results = X_test.copy()
results["Actual Price"] = y_test
results["Model Prediction"] = predictions
results["Baseline Prediction"] = baseline_predictions

print("\nTest Predictions")
print(results.round(2))


# Predict the price of a new house

new_house = pd.DataFrame({
    "area_sqft": [1500],
    "bedrooms": [3]
})

predicted_price = model.predict(new_house)

print("\nNew House Prediction")
print("Area: 1500 sq ft")
print("Bedrooms: 3")
print("Predicted Price:", round(predicted_price[0], 2), "lakh")


# Visualize actual vs predicted prices

plt.figure(figsize=(7, 5))

plt.scatter(
    y_test,
    predictions,
    label="Linear Regression"
)

lower = min(y_test.min(), predictions.min())
upper = max(y_test.max(), predictions.max())

plt.plot(
    [lower, upper],
    [lower, upper],
    linestyle="--",
    label="Perfect Predictions"
)

plt.xlabel("Actual Price (Lakh)")
plt.ylabel("Predicted Price (Lakh)")
plt.title("House Price Model Evaluation")
plt.legend()

plt.tight_layout()
plt.show()