import pandas as pd


students = pd.DataFrame({
    "Student": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Frank",
        "Grace",
        "Henry"
    ],
    "Python": [85, 72, 95, 64, 91, 78, 88, 69],
    "NumPy": [88, 70, 92, 60, 94, 82, 85, 73],
    "Pandas": [90, 68, 96, 62, 89, 80, 91, 71]
})


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"


def performance(row):
    if row["Average"] >= 90:
        return "Excellent"
    elif row["Average"] >= 80:
        return "Good"
    elif row["Average"] >= 70:
        return "Average"
    return "Needs Improvement"


students["Python_Grade"] = students["Python"].apply(grade)

students["NumPy_Grade"] = students["NumPy"].apply(grade)

students["Pandas_Grade"] = students["Pandas"].apply(grade)

students["Total"] = students.apply(
    lambda row:
        row["Python"] +
        row["NumPy"] +
        row["Pandas"],
    axis=1
)

students["Average"] = students.apply(
    lambda row:
        row["Total"] / 3,
    axis=1
)

students["Performance"] = students.apply(
    performance,
    axis=1
)

students["Result"] = students["Average"].apply(
    lambda score: "Pass" if score >= 70 else "Fail"
)

students["Student_Summary"] = students.apply(
    lambda row:
        row["Student"] +
        " - " +
        row["Performance"],
    axis=1
)

top_students = students[
    students["Average"] >= 85
].sort_values(
    by="Average",
    ascending=False
)

department_style_summary = students[
    ["Student", "Total", "Average", "Performance", "Result"]
].sort_values(
    by="Average",
    ascending=False
)

students.to_csv(
    "student_apply_analysis.csv",
    index=False
)

print(students)
print(top_students)
print(department_style_summary)