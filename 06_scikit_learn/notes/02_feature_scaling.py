import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, StandardScaler

data = pd.DataFrame({
    "area_sqft": [800, 900, 1000, 1100, 1200, 1300,
                  1400, 1500, 1600, 1700, 1800, 2000],
    "bedrooms": [2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4],
    "price_lakh": [35, 38, 42, 45, 50, 54,
                   58, 62, 67, 72, 78, 90]
})

X = data[["area_sqft", "bedrooms"]]
Y = data["price_lakh"]

X_train ,X_test ,Y_train , Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_scaled = pd.DataFrame(
    X_train_scaled,
    columns=X_train.columns,
    index=X_train.index
)
X_test_scaled = pd.DataFrame(
    X_test_scaled,
    columns=X_test.columns,
    index=X_test.index
)
print("Original Features")
print(X_train.head())

print("\nStandardized Features")
print(X_train_scaled.head())

print("\nMean Learned from Training Data")
print(scaler.mean_)

print("\nStandard Deviation Used by Scaler")
print(scaler.scale_)

print("\nScaled Training Feature Means")
print(X_train_scaled.mean().round(6))

print("\nScaled Training Feature Standard Deviations")
print(X_train_scaled.std(ddof=0).round(6))

print("\nScaled Test Features")
print(X_test_scaled)