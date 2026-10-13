import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


data = pd.DataFrame({
    "hours_studied": [
        1, 2, 3, 4, 5, 6, 7, 8,
        2, 3, 4, 5, 6, 7, 8, 9
    ],
    "exam_score": [
        32, 39, 47, 53, 61, 69, 77, 85,
        41, 46, 55, 63, 71, 79, 87, 94
    ]
})

X = data[["hours_studied"]]
y = data["exam_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

residuals = y_test.to_numpy() - predictions

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

results = pd.DataFrame({
    "Hours Studied": X_test["hours_studied"].to_numpy(),
    "Actual Score": y_test.to_numpy(),
    "Predicted Score": predictions,
    "Residual": residuals
})

print("Test Predictions")
print(results.round(2))

print("\nRegression Evaluation")
print("MAE:", round(mae, 2))
print("MSE:", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R²:", round(r2, 3))

