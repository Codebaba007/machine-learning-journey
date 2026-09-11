import pandas as pd

students = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 5, 6, 7, 8, 8],
    "Name": [
        "Alice", " Bob ", "Charlie", "David",
        "Emma", "Frank", "Grace", "Henry", "Henry"
    ],
    "Age": [
        "21", "22", "20", None,
        "19", "abc", "23", "21", "21"
    ],
    "Gender": [
        "Female", " male ", "MALE", None,
        "female", "Male", " FEMALE ", "male", "male"
    ],
    "Math": [85, 72, 91, 65, None, 78, 88, 74, 74],
    "Python": [90, 68, None, 70, 82, 80, 92, 76, 76],
    "Attendance": [
        "95%", "82%", "98%", "72%",
        "88%", "105%", "91%", "84%", "84%"
    ],
    "Department": [
        "CSE", "eee", "CSE", " BBA ",
        "EEE", "CSE", "cse", "EEE", "EEE"
    ]
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

top_students = students.nlargest(
    3,
    "Average_Score"
)

department_summary = (
    students
    .groupby("Department")
    .agg(
        Students=("Student_ID", "count"),
        Average_Score=("Average_Score", "mean"),
        Highest_Score=("Average_Score", "max"),
        Average_Attendance=("Attendance", "mean")
    )
    .reset_index()
)

performance_summary = (
    students["Performance"]
    .value_counts()
    .reset_index()
)

performance_summary.columns = [
    "Performance",
    "Students"
]

students.to_csv(
    "final_student_dataset.csv",
    index=False
)

department_summary.to_csv(
    "final_department_summary.csv",
    index=False
)

performance_summary.to_csv(
    "performance_summary.csv",
    index=False
)

print("Final Student Dataset")
print(students)

print("\nTop 3 Students")
print(top_students)

print("\nDepartment Summary")
print(department_summary)

print("\nPerformance Summary")
print(performance_summary)

print("\nFiles Saved")
print("final_student_dataset.csv")
print("final_department_summary.csv")
print("performance_summary.csv")