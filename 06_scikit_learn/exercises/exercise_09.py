
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

X = np.arange(1, 31).reshape(-1, 1)

rng = np.random.default_rng(7)
noise = rng.normal(0, 4, size=30)
y = 5 * X.ravel() + noise

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)
