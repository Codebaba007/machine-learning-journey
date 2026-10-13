import numpy as np
import pandas as pd
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


actual = np.array([100, 120, 150])
predicted = np.array([110, 115, 140])

residuals = actual - predicted

mae = mean_absolute_error(actual, predicted)
mse = mean_squared_error(actual, predicted)
rmse = np.sqrt(mse)
r2 = r2_score(actual, predicted)

results = pd.DataFrame({
    "Actual": actual,
    "Predicted": predicted,
    "Residual": residuals,
    "Absolute Error": np.abs(residuals),
    "Squared Error": residuals ** 2
})

print("Prediction Results")
print(results)

print("\nEvaluation Metrics")
print("MAE:", round(mae, 2))
print("MSE:", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R²:", round(r2, 3))