import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


data = pd.DataFrame({
    "area_sqft": [
        700, 800, 900, 1000, 1100, 1200,
        1300, 1400, 1500, 1600, 1700, 1800,
        900, 1100, 1300, 1500, 1700, 1900
    ],
    "bedrooms": [
        1, 2, 2, 2, 2, 3,
        3, 3, 3, 3, 4, 4,
        1, 2, 3, 3, 4, 4
    ],
    "price_lakh": [
        30, 35, 39, 43, 46, 52,
        56, 60, 64, 68, 75, 79,
        34, 45, 55, 66, 78, 85
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

print("Intercept:", round(model.intercept_, 4))

print("\nCoefficients")
for feature, coefficient in zip(X.columns, model.coef_):
    print(f"{feature}: {coefficient:.4f}")

results = X_test.copy()
results["Actual Price"] = y_test
results["Predicted Price"] = predictions
results["Residual"] = y_test - predictions

print("\nTest Predictions")
print(results.round(2))

mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:", round(mae, 2), "lakh")


new_house = pd.DataFrame({
    "area_sqft": [1500],
    "bedrooms": [3]
})

predicted_price = model.predict(new_house)

print("\nNew House")
print("Area: 1500 sq ft")
print("Bedrooms: 3")
print("Predicted price:", round(predicted_price[0], 2), "lakh")