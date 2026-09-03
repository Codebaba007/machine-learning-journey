import pandas as pd


# ============================================================
# Pandas Day 13 — Categorical Data Analyzer
# ============================================================


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
    "Department": [
        "CSE",
        "EEE",
        "CSE",
        "BBA",
        "EEE",
        "CSE",
        "BBA",
        "CSE"
    ],
    "Status": [
        "Active",
        "Inactive",
        "Active",
        "Active",
        "Inactive",
        "Active",
        "Active",
        "Inactive"
    ],
    "Performance": [
        "High",
        "Low",
        "Medium",
        "High",
        "Low",
        "Excellent",
        "Medium",
        "High"
    ]
})


print("PANDAS CATEGORICAL DATA ANALYZER")
print("================================")


# ============================================================
# 1. Original Data
# ============================================================

print("\nOriginal Data")
print("--------------------------------")
print(students)


# ============================================================
# 2. Convert Columns to Categories
# ============================================================

students["Department"] = (
    students["Department"].astype("category")
)

students["Status"] = (
    students["Status"].astype("category")
)

students["Performance"] = (
    students["Performance"].astype("category")
)


# ============================================================
# 3. Display Categories
# ============================================================

print("\nDepartment Categories")
print("--------------------------------")
print(students["Department"].cat.categories)

print("\nStatus Categories")
print("--------------------------------")
print(students["Status"].cat.categories)

print("\nPerformance Categories")
print("--------------------------------")
print(students["Performance"].cat.categories)


# ============================================================
# 4. Display Category Codes
# ============================================================

print("\nDepartment Category Codes")
print("--------------------------------")
print(students["Department"].cat.codes)


# ============================================================
# 5. Add a New Department Category
# ============================================================

students["Department"] = (
    students["Department"].cat.add_categories(["Civil"])
)

print("\nDepartments After Adding Civil")
print("--------------------------------")
print(students["Department"].cat.categories)


# ============================================================
# 6. Rename Status Categories
# ============================================================

students["Status"] = (
    students["Status"].cat.rename_categories({
        "Active": "Currently Active",
        "Inactive": "Currently Inactive"
    })
)

print("\nUpdated Status Categories")
print("--------------------------------")
print(students["Status"].cat.categories)


# ============================================================
# 7. Set Performance Categories
# ============================================================

students["Performance"] = (
    students["Performance"].cat.set_categories([
        "Low",
        "Medium",
        "High",
        "Excellent"
    ])
)


# ============================================================
# 8. Make Performance Ordered
# ============================================================

students["Performance"] = (
    students["Performance"].cat.set_categories(
        [
            "Low",
            "Medium",
            "High",
            "Excellent"
        ],
        ordered=True
    )
)


# ============================================================
# 9. Reorder Performance
# ============================================================

students["Performance"] = (
    students["Performance"].cat.reorder_categories([
        "Excellent",
        "High",
        "Medium",
        "Low"
    ])
)

print("\nPerformance Order")
print("--------------------------------")
print(students["Performance"].cat.categories)


# ============================================================
# 10. Count Students By Department
# ============================================================

print("\nStudents By Department")
print("--------------------------------")
print(
    students["Department"].value_counts()
)


# ============================================================
# 11. Count Students By Performance
# ============================================================

print("\nStudents By Performance")
print("--------------------------------")
print(
    students["Performance"].value_counts()
)


# ============================================================
# 12. Find High Performers
# ============================================================

high_performers = students[
    students["Performance"] == "High"
]

print("\nHigh Performers")
print("--------------------------------")
print(
    high_performers[
        ["Student", "Department", "Performance"]
    ]
)


# ============================================================
# 13. Find Excellent Students
# ============================================================

excellent_students = students[
    students["Performance"] == "Excellent"
]

print("\nExcellent Students")
print("--------------------------------")
print(
    excellent_students[
        ["Student", "Department", "Performance"]
    ]
)


# ============================================================
# 14. Sort By Performance
# ============================================================

sorted_students = students.sort_values(
    by="Performance"
)

print("\nStudents Sorted By Performance")
print("--------------------------------")
print(
    sorted_students[
        ["Student", "Performance"]
    ]
)


# ============================================================
# 15. Students By Department and Performance
# ============================================================

department_performance = pd.crosstab(
    students["Department"],
    students["Performance"]
)

print("\nDepartment vs Performance")
print("--------------------------------")
print(department_performance)


# ============================================================
# 16. Final Dataset
# ============================================================

print("\nFinal Dataset")
print("================================")
print(students)


# ============================================================
# 17. Export
# ============================================================

students.to_csv(
    "student_category_analysis.csv",
    index=False
)

print("\nSaved: student_category_analysis.csv")