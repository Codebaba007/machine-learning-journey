import pandas as pd


# ============================================================
# Pandas Day 12 — Text Data Exercise
# ============================================================


students = pd.DataFrame({
    "Student": [
        " Alice ",
        "BOB",
        " Charlie",
        "DAVID ",
        " eve "
    ],
    "Department": [
        " cse ",
        "EEE",
        "CSE",
        " eee ",
        "Cse"
    ],
    "Email": [
        "alice@gmail.com",
        "bob@yahoo.com",
        "charlie@gmail.com",
        "david@outlook.com",
        "eve@gmail.com"
    ],
    "Status": [
        "ACTIVE",
        "active",
        "INACTIVE",
        " Active ",
        "inactive"
    ]
})


# 1. Remove extra spaces from Student names

students["Student"] = (
    students["Student"].str.strip()
)


# 2. Convert Student names to Title Case

students["Student"] = (
    students["Student"].str.title()
)


# 3. Standardize Department names to uppercase

students["Department"] = (
    students["Department"]
    .str.strip()
    .str.upper()
)


# 4. Standardize Status to lowercase

students["Status"] = (
    students["Status"]
    .str.strip()
    .str.lower()
)


# 5. Find students using Gmail

gmail_students = students[
    students["Email"].str.endswith("@gmail.com")
]

print("Gmail Students")
print("====================")
print(
    gmail_students[
        ["Student", "Email"]
    ]
)


# 6. Find students whose name contains "a"

students_with_a = students[
    students["Student"]
    .str.lower()
    .str.contains("a")
]

print("\nStudents Whose Name Contains 'a'")
print("====================")
print(
    students_with_a[
        ["Student"]
    ]
)


# 7. Find CSE students

cse_students = students[
    students["Department"].str.startswith("CSE")
]

print("\nCSE Students")
print("====================")
print(
    cse_students[
        ["Student", "Department"]
    ]
)


# 8. Calculate name length

students["Name_Length"] = (
    students["Student"].str.len()
)

print("\nName Length")
print("====================")
print(
    students[
        ["Student", "Name_Length"]
    ]
)


# 9. Split email addresses

students["Email_Parts"] = (
    students["Email"].str.split("@")
)

print("\nEmail Parts")
print("====================")
print(
    students[
        ["Student", "Email_Parts"]
    ]
)


# 10. Extract email domain

students["Email_Domain"] = (
    students["Email"].str.extract(r"@(.+)")
)

print("\nEmail Domains")
print("====================")
print(
    students[
        ["Student", "Email_Domain"]
    ]
)


# 11. Replace inactive with not active

students["Status"] = (
    students["Status"]
    .str.replace("inactive", "not active")
)

print("\nUpdated Status")
print("====================")
print(
    students[
        ["Student", "Status"]
    ]
)


# 12. Final DataFrame

print("\nFinal Clean Data")
print("====================")
print(students)