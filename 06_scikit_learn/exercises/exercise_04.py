import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


data = pd.DataFrame({
    "hours_studied": [
        1, 2, 3, 4, 5, 6, 7, 8,
        2, 3, 4, 5, 6, 7, 8, 9
    ],
    "practice_tests": [
        1, 1, 2, 2, 3, 3, 4, 4,
        2, 2, 3, 3, 4, 4, 5, 5
    ],
    "exam_score": [
        32, 38, 47, 53, 62, 68, 78, 85,
        40, 45, 56, 64, 72, 80, 88, 94
    ]
})

X = data[["hours_studied", "practice_tests"]]
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

print("Intercept:", round(model.intercept_, 4))

print("\nLearned Coefficients")
for feature, coefficient in zip(X.columns, model.coef_):
    print(f"{feature}: {coefficient:.4f}")

results = X_test.copy()
results["Actual Score"] = y_test
results["Predicted Score"] = predictions
results["Residual"] = y_test - predictions

print("\nPredictions")
print(results.round(2))

mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:", round(mae, 2))


# Practice tasks

print("\nPractice Tasks")
print("1. Identify the coefficient for hours_studied.")
print("2. Identify the coefficient for practice_tests.")
print("3. Explain what the intercept represents.")
print("4. Explain the residual for one test observation.")
print("5. Change test_size to 0.3 and compare the results.")