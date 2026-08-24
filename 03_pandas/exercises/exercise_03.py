import pandas as pd
import numpy as np


students = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E"],
    "Python": [78, 67, np.nan, 90, 85],
    "NumPy": [85, np.nan, 81, 76, 91],
    "Math": [92, 95, 89, np.nan, 87]
})


# 1. Display Dataset

print("Original Dataset")
print("====================")
print(students)


# 2. Find Missing Values

print("\nMissing Values")
print("====================")
print(students.isnull())


# 3. Count Missing Values

print("\nMissing Count")
print("====================")
print(students.isnull().sum())


# 4. Count Non-Missing Values

print("\nNon-Missing Count")
print("====================")
print(students.notnull().sum())


# 5. Remove Rows With Missing Values

print("\nAfter dropna()")
print("====================")
print(students.dropna())


# 6. Fill Missing Values With 0

print("\nMissing Values Filled With 0")
print("====================")
print(students.fillna(0))


# 7. Fill Missing Values With Column Means

cleaned = students.copy()

for column in ["Python", "NumPy", "Math"]:
    cleaned[column] = cleaned[column].fillna(
        cleaned[column].mean()
    )

print("\nCleaned Dataset")
print("====================")
print(cleaned)


# 8. Verify No Missing Values Remain

print("\nMissing Values After Cleaning")
print("====================")
print(cleaned.isnull().sum())


# 9. Create Average Column

cleaned["Average"] = cleaned[
    ["Python", "NumPy", "Math"]
].mean(axis=1)

print("\nStudent Averages")
print("====================")
print(cleaned[["Student", "Average"]])


# 10. Students With Average >= 80

print("\nStudents With Average >= 80")
print("====================")

high_performers = cleaned[
    cleaned["Average"] >= 80
]

print(high_performers)