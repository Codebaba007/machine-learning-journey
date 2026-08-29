import pandas as pd


students = pd.DataFrame({
    " Student ": ["A", "B", "B", " C ", "D", "E"],
    "Python Score": ["78", "85", "85", "72", "90", "88"],
    "Status": ["pass", "PASS", "PASS", "fail", "Pass", "pass"]
})


# 1. Detect Duplicate Rows

print("Original Dataset")
print("====================")
print(students)

print("\nDuplicate Rows")
print("====================")
print(students.duplicated())


# 2. Count Duplicates

print("\nNumber of Duplicates")
print("====================")
print(students.duplicated().sum())


# 3. Remove Duplicates

students = students.drop_duplicates()

print("\nAfter Removing Duplicates")
print("====================")
print(students)


# 4. Clean Column Names

students.columns = students.columns.str.strip()

print("\nClean Column Names")
print("====================")
print(students)


# 5. Clean Student Names

students["Student"] = students["Student"].str.strip()

print("\nClean Student Names")
print("====================")
print(students)


# 6. Convert Python Score to Integer

students["Python Score"] = students["Python Score"].astype(int)

print("\nPython Data Type")
print("====================")
print(students.dtypes)


# 7. Standardize Status Values

students["Status"] = students["Status"].str.lower()

print("\nLowercase Status")
print("====================")
print(students)


# 8. Replace Status Values

students["Status"] = students["Status"].replace({
    "pass": "Passed",
    "fail": "Failed"
})

print("\nReplaced Status")
print("====================")
print(students)


# 9. Rename Column

students = students.rename(columns={
    "Python Score": "Python"
})

print("\nRenamed Column")
print("====================")
print(students)


# 10. Verify No Duplicates

print("\nFinal Duplicate Count")
print("====================")
print(students.duplicated().sum())


print("\nFinal Clean Dataset")
print("====================")
print(students)