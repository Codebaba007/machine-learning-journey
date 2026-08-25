import pandas as pd

students = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E"],
    "Python": [78, 67, 72, 90, 85],
    "NumPy": [85, 88, 81, 76, 91],
    "Math": [92, 95, 89, 84, 87]
})
print("Original Dataset")
print("====================")
print(students)

students["Total"] = students[["Python", "NumPy", "Math"]].sum(axis=1)
print("\nDataset after adding Total column") 
print("====================")
print(students)
students["Total"] = students[["Python", "NumPy", "Math"]].mean(axis=1)
print("\nDataset after adding Total column") 
print("====================")
print(students)
students["Status"] = students["Total"].apply(
    lambda x: "pass" if x >= 50 else "Fail"
)
print("\nWith Status")
print("====================")
print(students)

def grade(Total):
    if Total >= 90:
        return "A"
    elif Total >= 80:
        return "B"
    elif Total >= 70:
        return "C"
    elif Total >= 60:
        return "D"
    else:
        return "F"


students["Grade"] = students["Total"].apply(grade)

print("\nWith Grade")
print("====================")
print(students)

# 5. map()

students["Student"] = students["Student"].map(
    lambda x: "Student " + x
)

'''print("\nAfter map()")
print("====================")
print(students)
students = students.rename(columns={
    "Python": "Python_Marks",
    "NumPy": "NumPy_Marks",
    "Math": "Math_Marks"
})'''

print("\nRenamed Columns")
print("====================")
print(students)
print("\nSorted By Python")
print("====================")
print(
    students.sort_values(
        by="Python",
        ascending=False
    ))