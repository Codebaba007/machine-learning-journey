import pandas as pd


students = pd.DataFrame({
    " Student ": ["A", "B", "B", "C", "D", "E"],
    "Python Score": ["78", "85", "85", "72", "90", "88"],
    "Status": ["pass", "PASS", "PASS", "fail", "Pass", "pass"]
})


print("Original Dataset")
print("====================")
print(students)


# 1. Check Duplicate Rows

print("\nDuplicate Rows")
print("====================")
print(students.duplicated())


# 2. Count Duplicate Rows

print("\nNumber of Duplicates")
print("====================")
print(students.duplicated().sum())


# 3. Remove Duplicate Rows

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


# 6. Convert Python Score to Number

students["Python Score"] = students["Python Score"].astype(int)

print("\nConverted Data Type")
print("====================")
print(students.dtypes)


# 7. Standardize Status Values

students["Status"] = students["Status"].str.lower()

print("\nStandardized Status")
print("====================")
print(students)


# 8. Replace Values

students["Status"] = students["Status"].replace({
    "pass": "Passed",
    "fail": "Failed"
})

print("\nReplaced Status Values")
print("====================")
print(students)


# 9. Rename Column

students = students.rename(columns={
    "Python Score": "Python"
})

print("\nRenamed Column")
print("====================")
print(students)


# 10. Final Dataset

print("\nFinal Clean Dataset")
print("====================")
print(students)


# 11. Check for Duplicates Again

print("\nDuplicates After Cleaning")
print("====================")
print(students.duplicated().sum())