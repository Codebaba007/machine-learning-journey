import numpy as np

from sklearn.impute import SimpleImputer

X = np.array([
    [2.0, 70.0],
    [4.0, 85.0],
    [np.nan, 80.0],
    [6.0, np.nan],
    [3.0, 75.0]
])
print("Orginal Data:\n", X)

mean_imputer = SimpleImputer(strategy="mean")
X_mean = mean_imputer.fit_transform(X)

print("\nData after Mean Imputation:\n", X_mean)

median_imputer = SimpleImputer(strategy="median")
X_median = median_imputer.fit_transform(X)
print("\nData after Median Imputation:\n", X_median)

constant_imputer = SimpleImputer(strategy="constant", fill_value=0)
X_constant = constant_imputer.fit_transform(X)
print("\nData after Constant Imputation:\n", X_constant)

X_train = X[:4]
X_test = X[4:]
imputer = SimpleImputer(strategy="median")
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)
print("\nImputed Training Data:\n", X_train_imputed)
print("\nImputed Test Data:\n", X_test_imputed)
