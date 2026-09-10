import pandas as pd


# Raw dataset
students = pd.DataFrame({
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "Alice",
        "David",
        "Emma"
    ],
    "Age": [
        21,
        "22",
        20,
        21,
        None,
        19
    ],
    "Gender": [
        "Female",
        " male ",
        "MALE",
        "Female",
        "female",
        None
    ],
    "Score": [
        85,
        72,
        None,
        85,
        91,
        65
    ],
    "Attendance": [
        "95%",
        "82%",
        "98%",
        "95%",
        "105%",
        "70%"
    ],
    "Department": [
        "CSE",
        "EEE",
        "cse",
        "CSE",
        "BBA",
        " EEE "
    ]
})


print("Raw Dataset")
print(students)


# Inspect dataset
print("\nDataset Shape")
print(students.shape)

print("\nColumn Names")
print(students.columns)

print("\nData Types")
print(students.dtypes)

print("\nMissing Values")
print(students.isna().sum())

print("\nDuplicate Rows")
print(students.duplicated().sum())


# Convert Age to numeric
print("\nConverting Age")

students["Age"] = pd.to_numeric(
    students["Age"],
    errors="coerce"
)

print(students["Age"])


# Fill missing numerical values
print("\nHandling Missing Numerical Values")

students["Age"] = students["Age"].fillna(
    students["Age"].median()
)

students["Score"] = students["Score"].fillna(
    students["Score"].mean()
)

print(students)


# Clean Gender
print("\nCleaning Gender")

students["Gender"] = (
    students["Gender"]
    .str.strip()
    .str.lower()
    .str.title()
)

students["Gender"] = students["Gender"].fillna(
    students["Gender"].mode()[0]
)

print(students["Gender"])


# Clean Department
print("\nCleaning Department")

students["Department"] = (
    students["Department"]
    .str.strip()
    .str.upper()
)

print(students["Department"])


# Convert Attendance
print("\nConverting Attendance")

students["Attendance"] = (
    students["Attendance"]
    .str.replace("%", "", regex=False)
)

students["Attendance"] = pd.to_numeric(
    students["Attendance"],
    errors="coerce"
)

print(students["Attendance"])


# Limit invalid attendance values
print("\nFixing Attendance Range")

students["Attendance"] = students["Attendance"].clip(
    lower=0,
    upper=100
)

print(students["Attendance"])


# Remove duplicate rows
print("\nRemoving Duplicates")

students = students.drop_duplicates()

print(students)


# Create useful features
print("\nCreating Features")

students["Pass"] = (
    students["Score"] >= 50
).astype(int)

students["Performance"] = students["Score"].apply(
    lambda x: (
        "Excellent" if x >= 85
        else "Good" if x >= 70
        else "Needs Improvement"
    )
)

print(students)


# Validate cleaned dataset
print("\nFinal Data Types")
print(students.dtypes)

print("\nFinal Missing Values")
print(students.isna().sum())

print("\nFinal Dataset Shape")
print(students.shape)

print("\nCleaned ML-Ready Dataset")
print(students)


# Save dataset
students.to_csv(
    "students_ml_ready.csv",
    index=False
)

print("\nSaved students_ml_ready.csv")