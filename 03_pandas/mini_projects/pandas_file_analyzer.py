import pandas as pd
from pathlib import Path


# ============================================================
# Pandas Student File Analyzer
# ============================================================

input_file = Path("students.csv")
output_file = Path("students_analyzed.csv")


# ============================================================
# 1. Check File
# ============================================================

if not input_file.exists():
    print("Error: students.csv not found.")
    print("Run the Day 7 exercise first to create the file.")
    exit()


# ============================================================
# 2. Load CSV
# ============================================================

students = pd.read_csv(input_file)

print("STUDENT FILE ANALYZER")
print("============================")

print("\nLoaded Dataset")
print("----------------------------")
print(students)


# ============================================================
# 3. Dataset Information
# ============================================================

print("\nDataset Information")
print("----------------------------")
print("Rows:", students.shape[0])
print("Columns:", students.shape[1])
print("Column Names:", list(students.columns))


# ============================================================
# 4. Check Missing Values
# ============================================================

print("\nMissing Values")
print("----------------------------")
print(students.isnull().sum())


# ============================================================
# 5. Clean Missing Numerical Values
# ============================================================

for column in ["Python", "NumPy", "Math"]:
    students[column] = students[column].fillna(
        students[column].mean()
    )


# ============================================================
# 6. Calculate Total and Average
# ============================================================

students["Total"] = students[
    ["Python", "NumPy", "Math"]
].sum(axis=1)

students["Average"] = students[
    ["Python", "NumPy", "Math"]
].mean(axis=1)


# ============================================================
# 7. Assign Grade
# ============================================================

def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


students["Grade"] = students["Average"].apply(get_grade)


# ============================================================
# 8. Pass / Fail
# ============================================================

students["Status"] = students["Average"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)


# ============================================================
# 9. Sort By Average
# ============================================================

students = students.sort_values(
    by="Average",
    ascending=False
)


print("\nAnalyzed Dataset")
print("----------------------------")
print(students)


# ============================================================
# 10. Top 3 Students
# ============================================================

print("\nTop 3 Students")
print("----------------------------")

print(
    students[
        ["Student", "Average", "Grade"]
    ].head(3)
)


# ============================================================
# 11. High Performers
# ============================================================

print("\nStudents With Average >= 80")
print("----------------------------")

high_performers = students[
    students["Average"] >= 80
]

print(
    high_performers[
        ["Student", "Average", "Grade"]
    ]
)


# ============================================================
# 12. Class Statistics
# ============================================================

print("\nClass Statistics")
print("----------------------------")
print("Class Average:", students["Average"].mean())
print("Highest Average:", students["Average"].max())
print("Lowest Average:", students["Average"].min())


# ============================================================
# 13. Grade Distribution
# ============================================================

print("\nGrade Distribution")
print("----------------------------")
print(students["Grade"].value_counts())


# ============================================================
# 14. Save Analyzed Dataset
# ============================================================

students.to_csv(
    output_file,
    index=False
)

print("\nSaved:", output_file)


# ============================================================
# 15. Export Top Students
# ============================================================

students.head(3).to_csv(
    "top_students.csv",
    index=False
)

print("Saved: top_students.csv")