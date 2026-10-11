import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


data = pd.DataFrame({
    "practice_tests": [1, 2, 3, 4, 5, 6, 1, 3, 4, 6, 2, 5],
    "exam_score": [35, 43, 51, 60, 68, 77, 38, 53, 62, 79, 46, 70]
})

X = data[["practice_tests"]]
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

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)

results = pd.DataFrame({
    "Practice Tests": X_test["practice_tests"],
    "Actual Score": y_test,
    "Predicted Score": predictions
})

results["Residual"] = results["Actual Score"] - results["Predicted Score"]

print("\nResults")
print(results.round(2))

mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:", round(mae, 2))

