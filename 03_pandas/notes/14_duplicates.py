import pandas as pd


# ============================================================
# Pandas Day 14 — Working with Duplicate Data
# ============================================================


students = pd.DataFrame({
    "Student": [
        "Alice",
        "Bob",
        "Charlie",
        "Alice",
        "David",
        "Bob",
        "Eve",
        "Frank"
    ],
    "Department": [
        "CSE",
        "EEE",
        "CSE",
        "CSE",
        "BBA",
        "EEE",
        "CSE",
        "EEE"
    ],
    "Score": [
        85,
        72,
        90,
        85,
        78,
        72,
        95,
        88
    ]
})


print("ORIGINAL DATA")
print("====================")
print(students)


# ============================================================
# 1. Check for Duplicate Rows
# ============================================================

duplicates = students.duplicated()

print("\nDuplicate Rows")
print("====================")
print(duplicates)


# ============================================================
# 2. Show Duplicate Rows
# ============================================================

print("\nDuplicate Records")
print("====================")
print(
    students[
        students.duplicated()
    ]
)


# ============================================================
# 3. Count Duplicate Rows
# ============================================================

duplicate_count = students.duplicated().sum()

print("\nNumber of Duplicate Rows")
print("====================")
print(duplicate_count)


# ============================================================
# 4. Remove Duplicate Rows
# ============================================================

clean_students = students.drop_duplicates()

print("\nAfter Removing Duplicates")
print("====================")
print(clean_students)


# ============================================================
# 5. Find Duplicates Using Specific Columns
# ============================================================

duplicate_names = students.duplicated(
    subset=["Student"]
)

print("\nDuplicate Student Names")
print("====================")
print(duplicate_names)


# ============================================================
# 6. Show Records With Duplicate Names
# ============================================================

print("\nRecords With Duplicate Names")
print("====================")
print(
    students[
        students.duplicated(
            subset=["Student"],
            keep=False
        )
    ]
)


# ============================================================
# 7. keep="first"
# ============================================================

print("\nKeep First")
print("====================")
print(
    students[
        students.duplicated(
            subset=["Student"],
            keep="first"
        )
    ]
)


# ============================================================
# 8. keep="last"
# ============================================================

print("\nKeep Last")
print("====================")
print(
    students[
        students.duplicated(
            subset=["Student"],
            keep="last"
        )
    ]
)


# ============================================================
# 9. keep=False
# ============================================================

print("\nMark All Duplicates")
print("====================")
print(
    students[
        students.duplicated(
            subset=["Student"],
            keep=False
        )
    ]
)


# ============================================================
# 10. Remove Duplicates Using Specific Columns
# ============================================================

unique_students = students.drop_duplicates(
    subset=["Student"]
)

print("\nUnique Students")
print("====================")
print(unique_students)


# ============================================================
# 11. Keep Last Record
# ============================================================

latest_students = students.drop_duplicates(
    subset=["Student"],
    keep="last"
)

print("\nKeeping Last Student Record")
print("====================")
print(latest_students)


# ============================================================
# 12. Remove All Duplicate Groups
# ============================================================

no_duplicate_groups = students[
    ~students.duplicated(
        subset=["Student"],
        keep=False
    )
]

print("\nStudents Without Any Duplicate Names")
print("====================")
print(no_duplicate_groups)


# ============================================================
# 13. Sort Before Removing Duplicates
# ============================================================

sorted_students = students.sort_values(
    by="Score",
    ascending=False
)

best_records = sorted_students.drop_duplicates(
    subset=["Student"],
    keep="first"
)

print("\nBest Score For Each Student")
print("====================")
print(
    best_records[
        ["Student", "Department", "Score"]
    ]
)


# ============================================================
# 14. Final Clean Dataset
# ============================================================

final_students = students.drop_duplicates(
    subset=["Student"],
    keep="first"
)

print("\nFINAL DATASET")
print("====================")
print(final_students)


# ============================================================
# 15. Save Clean Dataset
# ============================================================

final_students.to_csv(
    "students_without_duplicates.csv",
    index=False
)

print("\nSaved: students_without_duplicates.csv")