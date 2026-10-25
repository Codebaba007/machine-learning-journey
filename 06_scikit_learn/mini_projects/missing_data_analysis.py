
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Features: area in square feet, bedrooms, age in years
X = np.array([
    [1000, 2, 10],
    [1200, 2, 8],
    [1500, 3, 5],
    [1800, 3, 4],
    [2000, 4, 3],
    [2200, 4, 2],
    [900,  2, 15],
    [1600, 3, np.nan],
    [1400, np.nan, 7],
    [np.nan, 4, 6],
    [2500, 5, 1],
    [1100, 2, np.nan],
], dtype=float)

# Illustrative prices in thousands of currency units
y = np.array([
    120, 140, 180, 220, 250, 280,
    100, 195, 165, 260, 320, 130
])

# Split before fitting preprocessing steps
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Preprocessing and model in one pipeline
model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression())
])

# Train the pipeline
model.fit(X_train, y_train)

# Predict prices for unseen test examples
predictions = model.predict(X_test)

print("Actual prices:", y_test)
print("Predicted prices:", np.round(predictions, 2))

mae = mean_absolute_error(y_test, predictions)
print(f"\nTest MAE: {mae:.2f}")

# Predict a new house with a missing age
new_house = np.array([[1700, 3, np.nan]])
predicted_price = model.predict(new_house)

print(
    "\nPredicted price for new house:",
    round(predicted_price[0], 2),
    "thousand currency units"
)
