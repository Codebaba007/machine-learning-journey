import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.DataFrame({
    "monthly_bill": [
        500, 1200, 700, 1500, 900, 1300,
        600, 1600, 800, 1400, 1000, 1700
    ],
    "complaints": [
        0, 4, 1, 5, 2, 4,
        0, 5, 1, 4, 2, 5
    ],
    "churn": [
        0, 1, 0, 1, 0, 1,
        0, 1, 0, 1, 0, 1
    ]
})

x = data[["monthly_bill", "complaints"]]
y = data["churn"]


x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.33,
    random_state=42,
    stratify=y
)
model = LogisticRegression()
model.fit(x_train, y_train)

predictions = model.predict(x_test)
probabilities = model.predict_proba(x_test)

results = x_test.copy()
results["Actual Churn"] = y_test
results["Predicted Churn"] = predictions
results["Churn Probability"] = probabilities[:, 1]

print(results.round(3))
print(results.to_string(index=False))