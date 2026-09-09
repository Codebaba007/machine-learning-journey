import pandas as pd

students = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Department": ["CSE", "EEE", "CSE", "BBA", "EEE"]
})

exam_1 = pd.DataFrame({
    "Student_ID": [1, 2, 3, 4],
    "Math": [85, 72, 91, 65],
    "Python": [90, 68, 95, 70]
})

exam_2 = pd.DataFrame({
    "Student_ID": [1, 2, 3, 5],
    "Math": [88, 75, 94, 82],
    "Python": [92, 71, 96, 85]
})

all_exams = pd.concat(
    [exam_1, exam_2],
    ignore_index=True
)

student_data = pd.merge(
    students,
    all_exams,
    on="Student_ID",
    how="left"
)

student_data["Math"] = student_data["Math"].fillna(0)
student_data["Python"] = student_data["Python"].fillna(0)

student_data["Average"] = (
    student_data["Math"] + student_data["Python"]
) / 2

student_data["Status"] = student_data["Average"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)

department_summary = (
    student_data
    .groupby("Department")["Average"]
    .agg(["count", "mean", "max"])
    .reset_index()
)

student_data = student_data.sort_values(
    "Average",
    ascending=False
)

student_data.to_csv(
    "combined_student_dataset.csv",
    index=False
)

department_summary.to_csv(
    "department_summary.csv",
    index=False
)

print("Combined Student Dataset")
print(student_data)

print("\nDepartment Summary")
print(department_summary)

print("\nFiles Saved")
print("combined_student_dataset.csv")
print("department_summary.csv")