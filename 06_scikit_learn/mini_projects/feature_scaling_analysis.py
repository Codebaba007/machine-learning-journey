import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


data = pd.DataFrame({
    "area_sqft": [
        650, 700, 750, 800, 850, 900, 950, 1000,
        1050, 1100, 1200, 1250, 1300, 1400, 1500, 1600
    ],
    "bedrooms": [
        1, 1, 2, 2, 2, 2, 2, 2,
        3, 3, 3, 3, 3, 3, 4, 4
    ],
    "price_lakh": [
        30, 33, 36, 39, 42, 45, 48, 51,
        55, 58, 64, 67, 70, 76, 83, 90
    ]
})

X = data[["area_sqft", "bedrooms"]]
y = data["price_lakh"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

X_train_scaled = pd.DataFrame(
    X_train_scaled,
    columns=X.columns,
    index=X_train.index
)

X_test_scaled = pd.DataFrame(
    X_test_scaled,
    columns=X.columns,
    index=X_test.index
)

print("Original Housing Data")
print(data.head())

print("\nOriginal Training Features")
print(X_train.head())

print("\nStandardized Training Features")
print(X_train_scaled.round(3))

print("\nStandardized Test Features")
print(X_test_scaled.round(3))

summary = pd.DataFrame({
    "Original Mean": X_train.mean(),
    "Original Std": X_train.std(ddof=0),
    "Scaled Mean": X_train_scaled.mean(),
    "Scaled Std": X_train_scaled.std(ddof=0)
})

print("\nFeature Scaling Summary")
print(summary.round(3))

print("\nTraining Observations:", len(X_train))
print("Testing Observations:", len(X_test))

print("\nTarget Example")
print(y_train.head())

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].boxplot(
    [X_train["area_sqft"], X_train["bedrooms"]],
    tick_labels=["Area", "Bedrooms"]
)
axes[0].set_title("Original Training Features")
axes[0].set_ylabel("Original Values")

axes[1].boxplot(
    [X_train_scaled["area_sqft"], X_train_scaled["bedrooms"]],
    tick_labels=["Area", "Bedrooms"]
)
axes[1].set_title("Standardized Training Features")
axes[1].set_ylabel("Standardized Values")

plt.tight_layout()
plt.show()