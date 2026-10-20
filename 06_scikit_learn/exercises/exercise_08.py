
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

X = np.arange(1, 31).reshape(-1, 1)

noise = np.array([
    1, -2, 2, 0, -1, 3, -2, 1, 0, -3,
    2, -1, 3, 0, -2, 1, -1, 2, -3, 1,
    0, -2, 3, -1, 2, 0, -3, 1, -1, 2
])

y = 5 * X.ravel() + noise

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# TODO: Create a shallow tree with max_depth=1.
# TODO: Create a deeper tree with max_depth=10.
# TODO: Train both models.
# TODO: Calculate training MAE and test MAE.
# TODO: Print and compare the results.

# Start your code here.
