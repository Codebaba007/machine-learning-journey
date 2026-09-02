import pandas as pd


# ============================================================
# Pandas Text Analyzer
# ============================================================


students = pd.DataFrame({
    "Student": [
        " Alice ",
        "BOB",
        " Charlie",
        "DAVID ",
        " eve ",
        "Frank"
    ],
    "Department": [
        " cse ",
        "EEE",
        "CSE",
        " eee ",
        "Cse",
        "CSE"
    ],
    "Email": [
        "alice@gmail.com",
        "bob@yahoo.com",
        "charlie@gmail.com",
        "david@outlook.com",
        "eve@gmail.com",
        "frank@yahoo.com"
    ],
    "Status": [
        "ACTIVE",
        "active",
        "INACTIVE",
        " Active ",
        "inactive",
        "ACTIVE"
    ]
})


print("PANDAS TEXT ANALYZER")
print("============================")


# ============================================================
# 1. Original Data
# ============================================================

print("\nOriginal Data")
print("----------------------------")
print(students)


# ============================================================
# 2. Clean Student Names
# ============================================================

students["Student"] = (
    students["Student"]
    .str.strip()
    .str.title()
)


# ============================================================
# 3. Clean Departments
# ============================================================

students["Department"] = (
    students["Department"]
    .str.strip()
    .str.upper()
)


# ============================================================
# 4. Clean Status
# ============================================================

students["Status"] = (
    students["Status"]
    .str.strip()
    .str.lower()
)


# ============================================================
# 5. Extract Email Username
# ============================================================

students["Username"] = (
    students["Email"]
    .str.split("@")
    .str[0]
)


# ============================================================
# 6. Extract Email Domain
# ============================================================

students["Email_Domain"] = (
    students["Email"]
    .str.extract(r"@(.+)")
)


# ============================================================
# 7. Calculate Name Length
# ============================================================

students["Name_Length"] = (
    students["Student"].str.len()
)


# ============================================================
# 8. Find Gmail Users
# ============================================================

gmail_students = students[
    students["Email"].str.endswith("@gmail.com")
]

print("\nGmail Students")
print("----------------------------")
print(
    gmail_students[
        ["Student", "Email"]
    ]
)


# ============================================================
# 9. Find CSE Students
# ============================================================

cse_students = students[
    students["Department"].str.startswith("CSE")
]

print("\nCSE Students")
print("----------------------------")
print(
    cse_students[
        ["Student", "Department"]
    ]
)


# ============================================================
# 10. Find Names Containing 'a'
# ============================================================

students_with_a = students[
    students["Student"]
    .str.lower()
    .str.contains("a")
]

print("\nStudents Whose Name Contains 'a'")
print("----------------------------")
print(
    students_with_a[
        ["Student"]
    ]
)


# ============================================================
# 11. Find Active Students
# ============================================================

active_students = students[
    students["Status"] == "active"
]

print("\nActive Students")
print("----------------------------")
print(
    active_students[
        ["Student", "Status"]
    ]
)


# ============================================================
# 12. Count Students By Department
# ============================================================

print("\nStudents By Department")
print("----------------------------")
print(
    students["Department"].value_counts()
)


# ============================================================
# 13. Count Students By Email Domain
# ============================================================

print("\nStudents By Email Domain")
print("----------------------------")
print(
    students["Email_Domain"].value_counts()
)


# ============================================================
# 14. Find Longest Name
# ============================================================

longest_name_index = students["Name_Length"].idxmax()

print("\nLongest Student Name")
print("----------------------------")
print(
    students.loc[
        longest_name_index,
        ["Student", "Name_Length"]
    ]
)


# ============================================================
# 15. Final Clean Dataset
# ============================================================

print("\nFinal Clean Dataset")
print("============================")
print(students)


# ============================================================
# 16. Save Results
# ============================================================

students.to_csv(
    "student_text_analysis.csv",
    index=False
)

print("\nSaved: student_text_analysis.csv")