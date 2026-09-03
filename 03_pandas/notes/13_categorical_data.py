import pandas as pd


# ============================================================
# Pandas Day 13 — Working with Categorical Data
# ============================================================


students = pd.DataFrame({
    "Student": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Frank"
    ],
    "Department": [
        "CSE",
        "EEE",
        "CSE",
        "BBA",
        "EEE",
        "CSE"
    ],
    "Status": [
        "Active",
        "Inactive",
        "Active",
        "Active",
        "Inactive",
        "Active"
    ],
    "Performance": [
        "High",
        "Low",
        "Medium",
        "High",
        "Low",
        "Medium"
    ]
})


print("ORIGINAL DATA")
print("====================")
print(students)


# ============================================================
# 1. Categorical Data
# ============================================================

# Department, Status, and Performance contain
# a limited number of repeated categories.

print("\nOriginal Data Types")
print("====================")
print(students.dtypes)


# ============================================================
# 2. Convert Column to Category
# ============================================================

students["Department"] = (
    students["Department"].astype("category")
)

print("\nDepartment Data Type")
print("====================")
print(students["Department"].dtype)


# ============================================================
# 3. View Categories
# ============================================================

print("\nDepartment Categories")
print("====================")
print(students["Department"].cat.categories)


# ============================================================
# 4. Category Codes
# ============================================================

print("\nDepartment Category Codes")
print("====================")
print(students["Department"].cat.codes)


# ============================================================
# 5. Convert More Columns to Category
# ============================================================

students["Status"] = (
    students["Status"].astype("category")
)

students["Performance"] = (
    students["Performance"].astype("category")
)

print("\nCategorical Data Types")
print("====================")
print(students.dtypes)


# ============================================================
# 6. Rename Categories
# ============================================================

students["Status"] = (
    students["Status"]
    .cat.rename_categories({
        "Active": "Currently Active",
        "Inactive": "Currently Inactive"
    })
)

print("\nRenamed Status Categories")
print("====================")
print(students["Status"])


# ============================================================
# 7. Add Categories
# ============================================================

students["Department"] = (
    students["Department"]
    .cat.add_categories(["Civil"])
)

print("\nAfter Adding Category")
print("====================")
print(students["Department"].cat.categories)


# ============================================================
# 8. Set Categories
# ============================================================

students["Performance"] = (
    students["Performance"]
    .cat.set_categories([
        "Low",
        "Medium",
        "High",
        "Excellent"
    ])
)

print("\nPerformance Categories")
print("====================")
print(students["Performance"].cat.categories)


# ============================================================
# 9. Ordered Categories
# ============================================================

performance_order = [
    "Low",
    "Medium",
    "High",
    "Excellent"
]

students["Performance"] = (
    students["Performance"]
    .cat.set_categories(
        performance_order,
        ordered=True
    )
)

print("\nOrdered Performance")
print("====================")
print(students["Performance"])


# ============================================================
# 10. Reorder Categories
# ============================================================

students["Performance"] = (
    students["Performance"]
    .cat.reorder_categories([
        "Excellent",
        "High",
        "Medium",
        "Low"
    ])
)

print("\nReordered Performance Categories")
print("====================")
print(students["Performance"].cat.categories)


# ============================================================
# 11. Remove Categories
# ============================================================

students["Department"] = (
    students["Department"]
    .cat.remove_categories(["Civil"])
)

print("\nAfter Removing Category")
print("====================")
print(students["Department"].cat.categories)


# ============================================================
# 12. Analyze Categorical Data
# ============================================================

print("\nStudents By Department")
print("====================")
print(
    students["Department"].value_counts()
)


print("\nStudents By Performance")
print("====================")
print(
    students["Performance"].value_counts()
)


# ============================================================
# 13. Filter Categorical Data
# ============================================================

high_performers = students[
    students["Performance"] == "High"
]

print("\nHigh Performers")
print("====================")
print(high_performers)


# ============================================================
# 14. Sort Ordered Categories
# ============================================================

sorted_students = students.sort_values(
    by="Performance"
)

print("\nSorted By Performance")
print("====================")
print(
    sorted_students[
        ["Student", "Performance"]
    ]
)


# ============================================================
# 15. Final Dataset
# ============================================================

print("\nFINAL DATA")
print("====================")
print(students)