
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

data = pd.DataFrame({
    "monthly_bill": [
        400, 500, 600, 700, 800, 900, 1000, 1100,
        1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900,
        450, 650, 750, 950, 1050, 1250, 1450, 1650
    ],
    "complaints": [
        0, 0, 1, 0, 1, 1, 0, 2,
        3, 3, 4, 4, 5, 5, 6, 6,
        0, 1, 1, 2, 2, 3, 4, 5
    ],
    "churn": [
        0, 0, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 1, 1, 1
    ]
})

X = data[["monthly_bill", "complaints"]]
y = data["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

predictions = model.predict(X_test_scaled)
probabilities = model.predict_proba(X_test_scaled)

results = X_test.copy()
results["Actual Churn"] = y_test
results["Predicted Churn"] = predictions
results["Churn Probability"] = probabilities[:, 1]

print(results.to_string(index=False))

new_customer = pd.DataFrame({
    "monthly_bill": [1250],
    "complaints": [3]
})

new_customer_scaled = scaler.transform(new_customer)
predicton = model.predict(new_customer_scaled)[0]
probability = model.predict_proba(new_customer_scaled)[0,1]

print("\nNew Customer Prediction: ")
print("Predicted Churn:", predicton)
print("Churn Probability:", round(probability, 3))