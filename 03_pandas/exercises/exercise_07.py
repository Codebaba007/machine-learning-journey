import pandas as pd


# 1. Create DataFrame

students = pd.DataFrame({
    "Student": [
        "Student 1", "Student 2", "Student 3",
        "Student 4", "Student 5", "Student 6",
        "Student 7", "Student 8", "Student 9",
        "Student 10"
    ],
    "Python": [78, 85, 72, 90, 88, 76, 95, 81, 69, 92],
    "NumPy": [85, 91, 81, 76, 94, 89, 90, 84, 73, 88],
    "Math": [92, 87, 89, 84, 91, 93, 96, 86, 75, 95]
})


# 2. Save as CSV

students.to_csv(
    "students.csv",
    index=False
)

print("Saved students.csv")


# 3. Read CSV

csv_data = pd.read_csv("students.csv")

print("\nCSV Data")
print(csv_data)


# 4. Save as Excel

students.to_excel(
    "students.xlsx",
    index=False
)

print("\nSaved students.xlsx")


# 5. Read Excel

excel_data = pd.read_excel("students.xlsx")

print("\nExcel Data")
print(excel_data)


# 6. Save as JSON

students.to_json(
    "students.json",
    orient="records",
    indent=4
)

print("\nSaved students.json")


# 7. Read JSON

json_data = pd.read_json("students.json")

print("\nJSON Data")
print(json_data)


# 8. Load Only Student and Python

selected = pd.read_csv(
    "students.csv",
    usecols=["Student", "Python"]
)

print("\nSelected Columns")
print(selected)


# 9. Shape and Column Names

print("\nShape:")
print(csv_data.shape)

print("\nColumns:")
print(list(csv_data.columns))


# 10. Create Average Column

students["Average"] = students[
    ["Python", "NumPy", "Math"]
].mean(axis=1)

print("\nFinal Data")
print(students)


# Save Final Dataset

students.to_csv(
    "students_final.csv",
    index=False
)

print("\nSaved students_final.csv")