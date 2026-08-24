import pandas as pd
import numpy as np

students = pd.DataFrame({
    "student": ["A", "B", "C", "D", "E"],
    "Python": [78, 67, np.nan, 90, 85],
    "NumPy": [85, np.nan, 81, 76, 91],
    "Math": [92, 95, 89, np.nan, 87]
})
print("Original DataFrame: ",students)
print("\nMissing Values: \n", students.isnull().sum())
print("\nNon-missing Values: \n", students.notnull().sum())

print("\nDrop rows with missing values: \n", students.dropna())
print("\nDrop columns with missing values: \n", students.dropna(axis=1))
print("\nFill missing values with 0: \n", students.fillna(0))

cleaned = students.copy()
cleaned["Python"] = cleaned["Python"].fillna(cleaned["Python"].mean())
cleaned["NumPy"] = cleaned["NumPy"].fillna(
    cleaned["NumPy"].mean()
)

cleaned["Math"] = cleaned["Math"].fillna(
    cleaned["Math"].mean()
)

print("\nMissing Values Filled With Column Mean")
print("====================")
print(cleaned)
print(cleaned.isnull().sum())

cleaned["Average"] = cleaned[["Python", "NumPy", "Math"]].mean(axis=1)
print("\nAverage Score: \n", cleaned)