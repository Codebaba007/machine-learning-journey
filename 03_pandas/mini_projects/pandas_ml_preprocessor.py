import pandas as pd

students = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 5, 6, 7],
    "Name": [
        "Alice", "Bob", "Charlie", "David",
        "Emma", "Frank", "Grace"
    ],
    "Age": ["21", "22", None, "23", "20", "abc", "21"],
    "Gender": [
        "Female", " male ", "MALE", None,
        "female", "Male", " FEMALE "
    ],
    "Math": [85, 72, 91, None, 78, 64, 88],
    "Python": [90, 68, None, 75, 82, 70, 92],
    "Attendance": [
        "95%", "82%", "98%", "88%",
        "105%", "65%", "91%"
    ],
    "Department": [
        "CSE", "eee", "CSE", " BBA ",
        "EEE", "cse", "CSE"
    ]
})

students["Age"] = pd.to_numeric(
    students["Age"],
    errors="coerce"
)

students["Age"] = students["Age"].fillna(
    students["Age"].median()
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

students["Average_Score"] = (
    students["Math"] + students["Python"]
) / 2

students["Pass"] = (
    (students["Average_Score"] >= 50) &
    (students["Attendance"] >= 75)
).astype(int)

students["Performance"] = students["Average_Score"].apply(
    lambda x: (
        "Excellent" if x >= 85
        else "Good" if x >= 70
        else "Needs Improvement"
    )
)

students = students.drop_duplicates()

students = students.sort_values(
    "Average_Score",
    ascending=False
)

department_summary = (
    students
    .groupby("Department")["Average_Score"]
    .agg(["count", "mean", "max"])
    .reset_index()
)

students.to_csv(
    "ml_ready_students.csv",
    index=False
)

department_summary.to_csv(
    "department_summary.csv",
    index=False
)

print("ML-Ready Student Dataset")
print(students)

print("\nDepartment Summary")
print(department_summary)

print("\nFiles Saved")
print("ml_ready_students.csv")
print("department_summary.csv")