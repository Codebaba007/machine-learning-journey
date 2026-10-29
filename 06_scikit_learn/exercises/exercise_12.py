
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

# Dataset: customer city
cities = [
    ["Dhaka"],
    ["Sylhet"],
    ["Chittagong"],
    ["Dhaka"],
    ["Sylhet"]
]

# 1. Create a OneHotEncoder
city_encoder = OneHotEncoder(sparse_output=False)

# 2. Fit and transform the city data
encoded_cities = city_encoder.fit_transform(cities)

# 3. Print the learned categories
print("City categories:")
print(city_encoder.categories_)

print("\nEncoded cities:")
print(encoded_cities)

# Dataset: customer satisfaction
levels = [
    ["Low"],
    ["High"],
    ["Medium"],
    ["Low"],
    ["High"]
]

# 4. Create an OrdinalEncoder with a specified order
level_encoder = OrdinalEncoder(
    categories=[["Low", "Medium", "High"]]
)

# 5. Fit and transform satisfaction data
encoded_levels = level_encoder.fit_transform(levels)

print("\nEncoded satisfaction levels:")
print(encoded_levels)

# 6. Create an encoder that ignores unknown categories
safe_encoder = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)

safe_encoder.fit([
    ["Dhaka"],
    ["Sylhet"]
])

# 7. Transform a city not seen during training
new_city = [["Rajshahi"]]
encoded_new_city = safe_encoder.transform(new_city)

print("\nEncoded unseen city:")
print(encoded_new_city)
