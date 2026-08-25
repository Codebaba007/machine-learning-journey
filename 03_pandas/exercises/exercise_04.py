import pandas as pd


students = pd.DataFrame({
    "Student": ["A", "B", "C", "D", "E"],
    "Python": [78, 67, 72, 90, 85],
    "NumPy": [85, 88, 81, 76, 91],
    "Math": [92, 95, 89, 84, 87]
})


# 1. Total

students["Total"] = students[
    ["Python", "NumPy", "Math"]
].sum(axis=1)


# 2. Average

students["Average"] = students[
    ["Python", "NumPy", "Math"]
].mean(axis=1)


# 3. Status

students["Status"] = students["Average"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)


# 4. Grade

def grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


students["Grade"] = students["Average"].apply(grade)


# 5. Rename Columns

students = students.rename(columns={
    "Python": "Python_Marks",
    "NumPy": "NumPy_Marks",
    "Math": "Math_Marks"
})


print("Transformed Dataset")
print("====================")
print(students)


# 6. Sort by Average — Highest First

print("\nSorted By Average")
print("====================")

print(
    students.sort_values(
        by="Average",
        ascending=False
    )
)


# 7. Sort by Python — Lowest First

print("\nSorted By Python")
print("====================")

print(
    students.sort_values(
        by="Python_Marks",
        ascending=True
    )
)


# 8. Students With Average >= 80

print("\nStudents With Average >= 80")
print("====================")

print(
    students[
        students["Average"] >= 80
    ]
)