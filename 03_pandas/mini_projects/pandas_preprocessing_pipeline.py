import pandas as pd
import numpy as np


# ============================================================
# Pandas Student Data Preprocessing Pipeline
# ============================================================

students = pd.DataFrame({
    " Student ": [
        "Student 1",
        "Student 2",
        "Student 2",
        " Student 3 ",
        "Student 4",
        "Student 5",
        "Student 6",
        "Student 7",
        "Student 8",
        "Student 9"
    ],
    "Python Score": [
        "78",
        "85",
        "85",
        "72",
        "90",
        np.nan,
        "74",
        "88",
        "81",
        "95"
    ],
    "NumPy Score": [
        "85",
        "91",
        "91",
        "81",
        "76",
        "89",
        "79",
        np.nan,
        "84",
        "90"
    ],
    "Math Score": [
        "92",
        "87",
        "87",
        "89",
        np.nan,
        "93",
        "82",
        "91",
        "86",
        "96"
    ],
    "Status": [
        "pass",
        "PASS",
        "PASS",
        "Pass",
        "fail",
        "PASS",
        "pass",
        "Pass",
        "PASS",
        "pass"
    ]
})


print("STUDENT DATA PREPROCESSING PIPELINE")
print("===================================")


# ============================================================
# 1. Original Dataset
# ============================================================

print("\nOriginal Dataset")
print("----------------------------")
print(students)


# ============================================================
# 2. Clean Column Names
# ============================================================

students.columns = students.columns.str.strip()

print("\nCleaned Column Names")
print("----------------------------")
print(list(students.columns))


# ============================================================
# 3. Remove Duplicate Rows
# ============================================================

print("\nDuplicate Count Before Cleaning")
print("----------------------------")
print(students.duplicated().sum())

students = students.drop_duplicates()

print("\nDuplicate Count After Cleaning")
print("----------------------------")
print(students.duplicated().sum())


# ============================================================
# 4. Clean Student Names
# ============================================================

students["Student"] = students["Student"].str.strip()


# ============================================================
# 5. Convert Scores to Numbers
# ============================================================

score_columns = [
    "Python Score",
    "NumPy Score",
    "Math Score"
]

for column in score_columns:
    students[column] = pd.to_numeric(
        students[column],
        errors="coerce"
    )


# ============================================================
# 6. Check Missing Values
# ============================================================

print("\nMissing Values")
print("----------------------------")
print(students.isnull().sum())


# ============================================================
# 7. Fill Missing Scores With Column Mean
# ============================================================

for column in score_columns:
    students[column] = students[column].fillna(
        students[column].mean()
    )


# ============================================================
# 8. Standardize Status
# ============================================================

students["Status"] = students["Status"].str.lower()

students["Status"] = students["Status"].replace({
    "pass": "Passed",
    "fail": "Failed"
})


# ============================================================
# 9. Rename Score Columns
# ============================================================

students = students.rename(columns={
    "Python Score": "Python",
    "NumPy Score": "NumPy",
    "Math Score": "Math"
})


# ============================================================
# 10. Create Total
# ============================================================

students["Total"] = students[
    ["Python", "NumPy", "Math"]
].sum(axis=1)


# ============================================================
# 11. Create Average
# ============================================================

students["Average"] = students[
    ["Python", "NumPy", "Math"]
].mean(axis=1)


# ============================================================
# 12. Create Grade
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
# 13. Sort By Average
# ============================================================

students = students.sort_values(
    by="Average",
    ascending=False
)


# ============================================================
# 14. Display Clean Dataset
# ============================================================

print("\nFinal Clean Dataset")
print("============================")
print(students)


# ============================================================
# 15. High Performers
# ============================================================

print("\nHigh Performers")
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
# 16. Final Checks
# ============================================================

print("\nFinal Checks")
print("----------------------------")
print("Duplicate Rows:", students.duplicated().sum())
print("Missing Values:")
print(students.isnull().sum())


# ============================================================
# 17. Export Clean Dataset
# ============================================================

students.to_csv(
    "students_cleaned.csv",
    index=False
)

print("\nSaved: students_cleaned.csv")