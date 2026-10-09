import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


data = pd.DataFrame({
    "area_sqft": [
        650, 700, 750, 800, 850, 900,
        950, 1000, 1050, 1100, 1150, 1200,
        1250, 1300, 1350, 1400, 1450, 1500,
        1550, 1600, 1650, 1700, 1750, 1800
    ],
    "bedrooms": [
        1, 1, 2, 2, 2, 2,
        2, 2, 3, 3, 3, 3,
        3, 3, 3, 3, 4, 4,
        4, 4, 4, 4, 4, 4
    ],
    "price_lakh": [
        32, 35, 38, 42, 45, 48,
        51, 54, 58, 62, 65, 69,
        72, 76, 79, 82, 87, 91,
        94, 98, 102, 105, 109, 113
    ]
})

X = data[["area_sqft", "bedrooms"]]
y = data["price_lakh"]

print("Housing Dataset")
print(data.head())

print("\nDataset shape:", data.shape)
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("\nTraining observations:", len(X_train))
print("Testing observations:", len(X_test))

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

results = X_test.copy()
results["Actual Price (Lakh)"] = y_test
results["Predicted Price (Lakh)"] = predictions

print("\nTest Predictions")
print(results.round(2))

mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:", round(mae, 2), "lakh")

plt.figure(figsize=(8, 5))

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
plt.title("Actual vs Predicted House Prices")

plt.tight_layout()
plt.show()