
import numpy as np

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Features: area, bedrooms, city
X = np.array([
    [1000, 2, "Dhaka"],
    [1200, 2, "Dhaka"],
    [1500, 3, "Dhaka"],
    [1800, 3, "Chittagong"],
    [2000, 4, "Chittagong"],
    [2200, 4, "Dhaka"],
    [900,  2, "Sylhet"],
    [1600, 3, "Sylhet"],
    [1400, 3, "Chittagong"],
    [2500, 5, "Dhaka"],
    [1100, 2, "Sylhet"],
    [1900, 4, "Chittagong"],
], dtype=object)

# Illustrative prices in thousands of currency units
y = np.array([
    120, 140, 180, 210, 250, 280,
    100, 170, 190, 320, 115, 240
])

# Split into training and test data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# Numerical features: columns 0 and 1
# Categorical feature: column 2
preprocessor = ColumnTransformer([
    ("numbers", StandardScaler(), [0, 1]),
    (
        "city",
        OneHotEncoder(handle_unknown="ignore"),
        [2]
    )
])

# Preprocessing + regression
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Train the model
model.fit(X_train, y_train)

# Predict test prices
predictions = model.predict(X_test)

print("Actual prices:")
print(y_test)

print("\nPredicted prices:")
print(np.round(predictions, 2))

# Evaluate using Mean Absolute Error
mae = mean_absolute_error(y_test, predictions)
print(f"\nTest MAE: {mae:.2f}")

# Predict for a new house in a city not seen during training
new_house = np.array([[1700, 3, "Rajshahi"]], dtype=object)

new_prediction = model.predict(new_house)

print("\nPredicted price for new house:")
print(f"{new_prediction[0]:.2f} thousand currency units")
