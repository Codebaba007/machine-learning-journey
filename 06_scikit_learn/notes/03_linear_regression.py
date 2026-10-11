import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


data = pd.DataFrame({
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 5, 7],
    "exam_score": [32, 40, 48, 55, 63, 70, 78, 85, 42, 46, 65, 80]
})

X = data[["hours_studied"]]
y = data["exam_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Slope (coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

print("\nPredictions")

results = pd.DataFrame({
    "Hours Studied": X_test["hours_studied"],
    "Actual Score": y_test,
    "Predicted Score": predictions
})

results["Residual"] = (
    results["Actual Score"] - results["Predicted Score"]
)

print(results.round(2))

mae = mean_absolute_error(y_test, predictions)

print("\nMean Absolute Error:", round(mae, 2))

new_student = pd.DataFrame({
    "hours_studied": [6]
})

predicted_score = model.predict(new_student)

print("\nPredicted score for 6 study hours:", round(predicted_score[0], 2))
