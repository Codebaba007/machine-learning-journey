
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

# Dataset: study hours, attendance, exam score
X = np.array([
    [2.0, 70.0],
    [4.0, 85.0],
    [np.nan, 80.0],
    [6.0, np.nan],
    [3.0, 75.0],
    [5.0, 90.0],
    [np.nan, 65.0],
    [7.0, 95.0],
])

y = np.array([55, 75, 68, 90, 60, 85, 50, 95])

# 1. Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# 2. Create a median imputer
imputer = SimpleImputer(strategy="median")

# 3. Learn medians from training data and fill missing values
X_train_filled = imputer.fit_transform(X_train)

# 4. Fill test data using the training medians
X_test_filled = imputer.transform(X_test)

# Display the results
print("Original training data:")
print(X_train)

print("\nTraining data after imputation:")
print(X_train_filled)

print("\nOriginal test data:")
print(X_test)

print("\nTest data after imputation:")
print(X_test_filled)

# 5. Check whether any missing values remain
print("\nMissing values in training data:")
print(np.isnan(X_train_filled).sum())

print("\nMissing values in test data:")
print(np.isnan(X_test_filled).sum())
