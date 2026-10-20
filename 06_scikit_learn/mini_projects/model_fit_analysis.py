
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

X = np.arange(1, 41).reshape(-1, 1)

rng = np.random.default_rng(42)
noise = rng.normal(0, 5, size=40)

y = 4 * X.ravel() + noise

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

depths = [1, 2, 3, 5, None]
results = []

for depth in depths:
    model = DecisionTreeRegressor(
        max_depth=depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_mae = mean_absolute_error(
        y_train, train_predictions
    )
    test_mae = mean_absolute_error(
        y_test, test_predictions
    )

    results.append({
        "Max Depth": str(depth),
        "Training MAE": round(train_mae, 2),
        "Test MAE": round(test_mae, 2),
        "Error Gap": round(test_mae - train_mae, 2)
    })

results_df = pd.DataFrame(results)

print("Model Complexity Analysis")
print(results_df.to_string(index=False))

print("\nInterpretation guide:")
print("- High training and test errors may indicate underfitting.")
print("- Low training error with much higher test error may indicate overfitting.")
print("- Lower test error can indicate better generalization.")
print("- Compare all results; do not judge by training error alone.")
