import pandas as pd


# ============================================================
# 1. Create a DataFrame
# ============================================================

students = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E"],
    "Python": [78, 85, 72, 90, 88],
    "Math": [92, 87, 89, 84, 91]
})

print("Original DataFrame")
print("====================")
print(students)


# ============================================================
# 2. Save to CSV
# ============================================================

students.to_csv(
    "students.csv",
    index=False
)

print("\nSaved: students.csv")


# ============================================================
# 3. Read CSV
# ============================================================

csv_data = pd.read_csv("students.csv")

print("\nRead CSV")
print("====================")
print(csv_data)


# ============================================================
# 4. Save to Excel
# ============================================================

students.to_excel(
    "students.xlsx",
    index=False
)

print("\nSaved: students.xlsx")


# ============================================================
# 5. Read Excel
# ============================================================

excel_data = pd.read_excel("students.xlsx")

print("\nRead Excel")
print("====================")
print(excel_data)


# ============================================================
# 6. Save to JSON
# ============================================================

students.to_json(
    "students.json",
    orient="records",
    indent=4
)

print("\nSaved: students.json")


# ============================================================
# 7. Read JSON
# ============================================================

json_data = pd.read_json("students.json")

print("\nRead JSON")
print("====================")
print(json_data)


# ============================================================
# 8. Inspect Imported Data
# ============================================================

print("\nImported Data Information")
print("====================")

print("Shape:", csv_data.shape)
print("Columns:", list(csv_data.columns))
print("Data Types:")
print(csv_data.dtypes)


# ============================================================
# 9. Read Only Selected CSV Columns
# ============================================================

selected = pd.read_csv(
    "students.csv",
    usecols=["Student", "Python"]
)

print("\nSelected CSV Columns")
print("====================")
print(selected)


# ============================================================
# 10. SQL Concept
# ============================================================

# Pandas can also read data from SQL databases:
#
# pd.read_sql(query, connection)
#
# This allows database data to be loaded into a DataFrame.