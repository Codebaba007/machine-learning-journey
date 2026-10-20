
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

X = np.arange(1, 21).reshape(-1, 1)

noise = np.array([
    2, -1, 1, 0, -2, 3, -1, 2, 0, -3,
    1, -2, 3, 0, -1, 2, -3, 1, 0, 2
])

y = 3 * X.ravel() + noise

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

models = {
    "Shallow Tree": DecisionTreeRegressor(
        max_depth=1,
        random_state=42
    ),
    "Medium Tree": DecisionTreeRegressor(
        max_depth=3,
        random_state=42
    ),
    "Deep Tree": DecisionTreeRegressor(
        max_depth=None,
        random_state=42
    )
}

for name, model in models.items():
    model.fit(X_train, y_train)

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_mae = mean_absolute_error(
        y_train, train_predictions
    )
    test_mae = mean_absolute_error(
        y_test, test_predictions
    )

    print(f"\n{name}")
    print(f"Training MAE: {train_mae:.2f}")
    print(f"Test MAE:     {test_mae:.2f}")
