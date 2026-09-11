import pandas as pd


# Raw student data
students = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 5, 6, 6],
    "Name": [
        "Alice",
        " Bob ",
        "Charlie",
        "David",
        "Emma",
        "Frank",
        "Frank"
    ],
    "Age": ["21", "22", None, "23", "20", "abc", "abc"],
    "Gender": [
        "Female",
        " male ",
        "MALE",
        None,
        "female",
        "Male",
        "Male"
    ],
    "Math": [85, 72, 91, None, 78, 64, 64],
    "Python": [90, 68, None, 75, 82, 70, 70],
    "Attendance": [
        "95%",
        "82%",
        "98%",
        "88%",
        "105%",
        "65%",
        "65%"
    ],
    "Department": [
        "CSE",
        "eee",
        "CSE",
        " BBA ",
        "EEE",
        "cse",
        "cse"
    ]
})


print("Raw Dataset")
print(students)


# Inspect the dataset
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


# Clean text columns
print("\nCleaning Text")

students["Name"] = students["Name"].str.strip()

students["Gender"] = (
    students["Gender"]
    .str.strip()
    .str.lower()
    .str.title()
)

students["Department"] = (
    students["Department"]
    .str.strip()
    .str.upper()
)

students["Gender"] = students["Gender"].fillna(
    students["Gender"].mode()[0]
)

print(students)


# Convert Age to numeric
print("\nConverting Age")

students["Age"] = pd.to_numeric(
    students["Age"],
    errors="coerce"
)

students["Age"] = students["Age"].fillna(
    students["Age"].median()
)

print(students["Age"])


# Handle missing scores
print("\nHandling Missing Scores")

students["Math"] = students["Math"].fillna(
    students["Math"].mean()
)

students["Python"] = students["Python"].fillna(
    students["Python"].mean()
)

print(students)


# Convert attendance to numeric
print("\nConverting Attendance")

students["Attendance"] = (
    students["Attendance"]
    .str.replace("%", "", regex=False)
)

students["Attendance"] = pd.to_numeric(
    students["Attendance"],
    errors="coerce"
)

students["Attendance"] = students["Attendance"].clip(
    lower=0,
    upper=100
)

print(students["Attendance"])


# Remove duplicates
print("\nRemoving Duplicates")

students = students.drop_duplicates(
    subset=["Student_ID"]
)

print(students)


# Create features
print("\nCreating Features")

students["Average_Score"] = (
    students["Math"] + students["Python"]
) / 2

students["Pass"] = (
    (
        students["Average_Score"] >= 50
    ) &
    (
        students["Attendance"] >= 75
    )
).astype(int)

students["Performance"] = students["Average_Score"].apply(
    lambda x: (
        "Excellent" if x >= 85
        else "Good" if x >= 70
        else "Needs Improvement"
    )
)

print(students)


# Filter useful records
print("\nFiltering Students")

eligible_students = students.query(
    "Attendance >= 75"
)

print(eligible_students)


# Sort students
print("\nSorting Students")

eligible_students = eligible_students.sort_values(
    "Average_Score",
    ascending=False
)

print(eligible_students)


# Department analysis
print("\nDepartment Analysis")

department_summary = (
    eligible_students
    .groupby("Department")["Average_Score"]
    .agg(["count", "mean", "max"])
    .reset_index()
)

print(department_summary)


# Top students
print("\nTop 3 Students")

top_students = eligible_students.nlargest(
    3,
    "Average_Score"
)

print(top_students)


# Final validation
print("\nFinal Validation")

print("Shape:")
print(eligible_students.shape)

print("\nMissing Values:")
print(eligible_students.isna().sum())

print("\nData Types:")
print(eligible_students.dtypes)


# Save final datasets
eligible_students.to_csv(
    "final_ml_ready_students.csv",
    index=False
)

department_summary.to_csv(
    "final_department_summary.csv",
    index=False
)

print("\nFiles Saved")
print("final_ml_ready_students.csv")
print("final_department_summary.csv")