import pandas as pd


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


# 1. Convert columns to categorical

students["Department"] = (
    students["Department"].astype("category")
)

students["Status"] = (
    students["Status"].astype("category")
)

students["Performance"] = (
    students["Performance"].astype("category")
)


# 2. Print Department categories

print("Department Categories")
print("====================")
print(students["Department"].cat.categories)


# 3. Print Department codes

print("\nDepartment Codes")
print("====================")
print(students["Department"].cat.codes)


# 4. Rename Status categories

students["Status"] = (
    students["Status"].cat.rename_categories({
        "Active": "Currently Active",
        "Inactive": "Currently Inactive"
    })
)

print("\nUpdated Status")
print("====================")
print(students["Status"])


# 5. Add Civil category

students["Department"] = (
    students["Department"].cat.add_categories(["Civil"])
)

print("\nDepartment Categories After Adding Civil")
print("====================")
print(students["Department"].cat.categories)


# 6. Set Performance categories

students["Performance"] = (
    students["Performance"].cat.set_categories([
        "Low",
        "Medium",
        "High",
        "Excellent"
    ])
)


# 7. Make Performance ordered

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


# 8. Reorder Performance

students["Performance"] = (
    students["Performance"].cat.reorder_categories([
        "Excellent",
        "High",
        "Medium",
        "Low"
    ])
)


print("\nPerformance Categories")
print("====================")
print(students["Performance"].cat.categories)


# 9. Count students by Department

print("\nStudents By Department")
print("====================")
print(students["Department"].value_counts())


# 10. Filter High Performers

high_performers = students[
    students["Performance"] == "High"
]

print("\nHigh Performers")
print("====================")
print(high_performers)


# 11. Sort by Performance

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


# 12. Final DataFrame

print("\nFinal DataFrame")
print("====================")
print(students)