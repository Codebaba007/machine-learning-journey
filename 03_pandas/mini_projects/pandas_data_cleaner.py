import pandas as pd
import numpy as np


students = pd.DataFrame({
    "Student": [
        "Student 1",
        "Student 2",
        "Student 3",
        "Student 4",
        "Student 5",
        "Student 6",
        "Student 7",
        "Student 8",
        "Student 9",
        "Student 10"
    ],
    "Python": [78, 67, np.nan, 90, 85, 92, 74, np.nan, 81, 95],
    "NumPy": [85, np.nan, 81, 76, 91, 89, np.nan, 94, 84, 90],
    "Math": [92, 95, 89, np.nan, 87, 93, 82, 91, np.nan, 96]
})


print("PANDAS STUDENT DATA CLEANER")
print("============================")


# 1. Original Dataset

print("\nOriginal Dataset")
print("----------------------------")
print(students)


# 2. Missing Value Detection

print("\nMissing Values")
print("----------------------------")
print(students.isnull())


# 3. Missing Value Count

print("\nMissing Values By Column")
print("----------------------------")
print(students.isnull().sum())


# 4. Remove Incomplete Rows

print("\nComplete Rows Only")
print("----------------------------")
print(students.dropna())


# 5. Create Clean Copy

cleaned = students.copy()


# 6. Fill Missing Values With Column Means

for column in ["Python", "NumPy", "Math"]:
    cleaned[column] = cleaned[column].fillna(
        cleaned[column].mean()
    )


# 7. Display Cleaned Dataset

print("\nCleaned Dataset")
print("----------------------------")
print(cleaned)


# 8. Verify Cleaning

print("\nMissing Values After Cleaning")
print("----------------------------")
print(cleaned.isnull().sum())


# 9. Calculate Student Average

cleaned["Average"] = cleaned[
    ["Python", "NumPy", "Math"]
].mean(axis=1)

print("\nStudent Averages")
print("----------------------------")
print(cleaned[["Student", "Average"]])


# 10. Students With Average >= 80

print("\nStudents With Average >= 80")
print("----------------------------")

high_performers = cleaned[
    cleaned["Average"] >= 80
]

print(high_performers[["Student", "Average"]])


# 11. Best Student

best_student_index = cleaned["Average"].idxmax()

print("\nBest Student")
print("----------------------------")
print("Student:", cleaned.loc[best_student_index, "Student"])
print("Average:", cleaned.loc[best_student_index, "Average"])


# 12. Final Statistics

print("\nFinal Statistics")
print("----------------------------")
print("Overall Average:", cleaned["Average"].mean())
print("Highest Average:", cleaned["Average"].max())
print("Lowest Average:", cleaned["Average"].min())