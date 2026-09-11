import pandas as pd

students = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 5, 5],
    "Name": ["Alice", " Bob ", "Charlie", "David", "Emma", "Emma"],
    "Age": ["21", "22", None, "abc", "20", "20"],
    "Gender": ["Female", " male ", "MALE", None, "female", "female"],
    "Math": [85, 72, 91, None, 78, 78],
    "Python": [90, 68, None, 75, 82, 82],
    "Attendance": ["95%", "82%", "98%", "88%", "105%", "105%"],
    "Department": ["CSE", "eee", "CSE", " BBA ", "EEE", "EEE"]
})

students["Name"] = students["Name"].str.strip()

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

students["Age"] = pd.to_numeric(
    students["Age"],
    errors="coerce"
)

students["Age"] = students["Age"].fillna(
    students["Age"].median()
)

students["Math"] = students["Math"].fillna(
    students["Math"].mean()
)

students["Python"] = students["Python"].fillna(
    students["Python"].mean()
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

students = students.drop_duplicates(
    subset=["Student_ID"]
)

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

students = students.sort_values(
    "Average_Score",
    ascending=False
)

print("Cleaned Dataset")
print(students)

print("\nTop 3 Students")
print(students.nlargest(3, "Average_Score"))

print("\nDepartment Summary")
print(
    students
    .groupby("Department")["Average_Score"]
    .agg(["count", "mean", "max"])
    .reset_index()
)

print("\nMissing Values")
print(students.isna().sum())