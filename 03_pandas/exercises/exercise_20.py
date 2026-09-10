import pandas as pd

students = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Alice", "David", "Emma"],
    "Age": ["21", "22", None, "21", "24", "19"],
    "Gender": [" female ", "MALE", "Male", "female", None, "FEMALE"],
    "Score": [85, 72, None, 85, 91, 65],
    "Attendance": ["95%", "82%", "98%", "95%", "105%", "70%"],
    "Department": ["cse", "EEE", "CSE", "cse", " bba ", "EEE"]
})

students["Age"] = pd.to_numeric(
    students["Age"],
    errors="coerce"
)

students["Age"] = students["Age"].fillna(
    students["Age"].median()
)

students["Score"] = students["Score"].fillna(
    students["Score"].mean()
)

students["Gender"] = (
    students["Gender"]
    .str.strip()
    .str.lower()
    .str.title()
)

students["Gender"] = students["Gender"].fillna(
    students["Gender"].mode()[0]
)

students["Department"] = (
    students["Department"]
    .str.strip()
    .str.upper()
)

students["Attendance"] = (
    students["Attendance"]
    .str.replace("%", "", regex=False)
)

students["Attendance"] = pd.to_numeric(
    students["Attendance"],
    errors="coerce"
)

students["Attendance"] = students["Attendance"].clip(
    0,
    100
)

students = students.drop_duplicates()

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

print("Cleaned Dataset")
print(students)

print("\nMissing Values")
print(students.isna().sum())

print("\nData Types")
print(students.dtypes)