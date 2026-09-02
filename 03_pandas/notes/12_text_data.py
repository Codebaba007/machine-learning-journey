import pandas as pd


# ============================================================
# Pandas Day 12 — Working with Text Data
# ============================================================


students = pd.DataFrame({
    "Student": [
        " Alice ",
        "BOB",
        "Charlie",
        " DAVID ",
        "eve"
    ],
    "Department": [
        " CSE",
        "cse ",
        "CSE",
        " EEE ",
        "eee"
    ],
    "Email": [
        "alice@gmail.com",
        "bob@yahoo.com",
        "charlie@gmail.com",
        "david@outlook.com",
        "eve@gmail.com"
    ],
    "Status": [
        "Active",
        "active",
        "INACTIVE",
        "Active",
        "inactive"
    ]
})


print("ORIGINAL DATA")
print("====================")
print(students)


# ============================================================
# 1. .str Accessor
# ============================================================

# .str gives access to Pandas string operations.

print("\n.str Accessor")
print("====================")
print(students["Department"].str)


# ============================================================
# 2. .str.lower()
# ============================================================

# Convert all text to lowercase.

students["Department_Lower"] = (
    students["Department"].str.lower()
)

print("\nLowercase")
print("====================")
print(
    students[
        ["Department", "Department_Lower"]
    ]
)


# ============================================================
# 3. .str.upper()
# ============================================================

# Convert all text to uppercase.

students["Department_Upper"] = (
    students["Department"].str.upper()
)

print("\nUppercase")
print("====================")
print(
    students[
        ["Department", "Department_Upper"]
    ]
)


# ============================================================
# 4. .str.strip()
# ============================================================

# Remove spaces from the beginning and end of text.

students["Clean_Department"] = (
    students["Department"].str.strip()
)

print("\nStrip Spaces")
print("====================")
print(
    students[
        ["Department", "Clean_Department"]
    ]
)


# ============================================================
# 5. .str.replace()
# ============================================================

# Replace one piece of text with another.

students["Clean_Status"] = (
    students["Status"]
    .str.lower()
    .str.replace("inactive", "not active")
)

print("\nReplace Text")
print("====================")
print(
    students[
        ["Status", "Clean_Status"]
    ]
)


# ============================================================
# 6. .str.contains()
# ============================================================

# Check whether text contains a specific value.

gmail_students = students[
    students["Email"].str.contains("@gmail.com")
]

print("\nGmail Students")
print("====================")
print(
    gmail_students[
        ["Student", "Email"]
    ]
)


# ============================================================
# 7. .str.startswith()
# ============================================================

# Check whether text starts with a specific value.

cse_students = students[
    students["Department"]
    .str.strip()
    .str.upper()
    .str.startswith("CSE")
]

print("\nCSE Students")
print("====================")
print(
    cse_students[
        ["Student", "Department"]
    ]
)


# ============================================================
# 8. .str.endswith()
# ============================================================

# Check whether text ends with a specific value.

gmail_students = students[
    students["Email"].str.endswith("@gmail.com")
]

print("\nStudents With Gmail")
print("====================")
print(
    gmail_students[
        ["Student", "Email"]
    ]
)


# ============================================================
# 9. .str.len()
# ============================================================

# Find the number of characters in each string.

students["Name_Length"] = (
    students["Student"].str.strip().str.len()
)

print("\nName Length")
print("====================")
print(
    students[
        ["Student", "Name_Length"]
    ]
)


# ============================================================
# 10. .str.split()
# ============================================================

# Split a string into separate pieces.

students["Email_Parts"] = (
    students["Email"].str.split("@")
)

print("\nSplit Email")
print("====================")
print(
    students[
        ["Email", "Email_Parts"]
    ]
)


# Extract the username from the email.

students["Username"] = (
    students["Email"].str.split("@").str[0]
)

print("\nEmail Username")
print("====================")
print(
    students[
        ["Email", "Username"]
    ]
)


# Extract the domain from the email.

students["Email_Domain"] = (
    students["Email"].str.split("@").str[1]
)

print("\nEmail Domain")
print("====================")
print(
    students[
        ["Email", "Email_Domain"]
    ]
)


# ============================================================
# 11. .str.extract()
# ============================================================

# Extract a specific pattern from text.

students["Domain_Extracted"] = (
    students["Email"].str.extract(
        r"@(.+)"
    )
)

print("\nExtracted Email Domain")
print("====================")
print(
    students[
        ["Email", "Domain_Extracted"]
    ]
)


# ============================================================
# 12. Combining String Operations
# ============================================================

# Multiple string operations can be chained together.

students["Clean_Name"] = (
    students["Student"]
    .str.strip()
    .str.lower()
)

students["Clean_Department_Final"] = (
    students["Department"]
    .str.strip()
    .str.upper()
)

students["Clean_Status_Final"] = (
    students["Status"]
    .str.strip()
    .str.lower()
)


print("\nCleaned Text")
print("====================")
print(
    students[
        [
            "Clean_Name",
            "Clean_Department_Final",
            "Clean_Status_Final"
        ]
    ]
)


# ============================================================
# 13. Practical Text Filtering
# ============================================================

# Find students whose name contains the letter "a".

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


# ============================================================
# 14. Standardize Text Data
# ============================================================

# Create clean standardized columns.

students["Student"] = (
    students["Student"]
    .str.strip()
    .str.title()
)

students["Department"] = (
    students["Department"]
    .str.strip()
    .str.upper()
)

students["Status"] = (
    students["Status"]
    .str.strip()
    .str.lower()
)


# ============================================================
# 15. Final Clean Dataset
# ============================================================

print("\nFINAL CLEAN DATA")
print("====================")
print(
    students[
        [
            "Student",
            "Department",
            "Email",
            "Status"
        ]
    ]
)