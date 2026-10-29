
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

# -----------------------------------
# 1. OneHotEncoder
# -----------------------------------

cities = [
    ["Dhaka"],
    ["Sylhet"],
    ["Chittagong"],
    ["Dhaka"]
]

one_hot = OneHotEncoder(sparse_output=False)

encoded_cities = one_hot.fit_transform(cities)

print("City categories:")
print(one_hot.categories_)

print("\nOne-hot encoded cities:")
print(encoded_cities)

# -----------------------------------
# 2. OrdinalEncoder
# -----------------------------------

satisfaction = [
    ["Low"],
    ["Medium"],
    ["High"],
    ["Low"]
]

ordinal = OrdinalEncoder(
    categories=[["Low", "Medium", "High"]]
)

encoded_satisfaction = ordinal.fit_transform(satisfaction)

print("\nOriginal satisfaction levels:")
print(satisfaction)

print("\nOrdinal encoded satisfaction:")
print(encoded_satisfaction)

# -----------------------------------
# 3. Handling unknown categories
# -----------------------------------

city_encoder = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)

city_encoder.fit([
    ["Dhaka"],
    ["Sylhet"],
    ["Dhaka"]
])

new_cities = [
    ["Rajshahi"],
    ["Dhaka"]
]

encoded_new_cities = city_encoder.transform(new_cities)

print("\nNew cities:")
print(new_cities)

print("\nEncoded new cities:")
print(encoded_new_cities)
