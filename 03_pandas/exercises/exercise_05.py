import pandas as pd


students = pd.DataFrame({
    "Student": [
        "Student 1", "Student 2", "Student 3",
        "Student 4", "Student 5", "Student 6",
        "Student 7", "Student 8", "Student 9",
        "Student 10"
    ],
    "Department": [
        "Science", "Science", "Arts", "Arts", "Science",
        "Commerce", "Commerce", "Science", "Arts", "Commerce"
    ],
    "Python": [78, 67, 72, 90, 85, 92, 74, 88, 81, 95],
    "NumPy": [85, 88, 81, 76, 91, 89, 79, 94, 84, 90],
    "Math": [92, 95, 89, 84, 87, 93, 82, 91, 86, 96]
})


# 1. Group students by Department

grouped = students.groupby("Department")

print("Grouped Data")
print("====================")
print(grouped)


# 2. Average Python mark by Department

print("\nAverage Python By Department")
print("====================")
print(
    grouped["Python"].mean()
)


# 3. Average of all subjects by Department

print("\nSubject Averages By Department")
print("====================")
print(
    grouped[["Python", "NumPy", "Math"]].mean()
)


# 4. Total marks by Department

print("\nTotal Marks By Department")
print("====================")
print(
    grouped[["Python", "NumPy", "Math"]].sum()
)


# 5. Highest marks by Department

print("\nHighest Marks By Department")
print("====================")
print(
    grouped[["Python", "NumPy", "Math"]].max()
)


# 6. Lowest marks by Department

print("\nLowest Marks By Department")
print("====================")
print(
    grouped[["Python", "NumPy", "Math"]].min()
)


# 7. Count students in each Department

print("\nStudent Count By Department")
print("====================")
print(
    grouped["Student"].count()
)


# 8. Multiple aggregations

print("\nPython Multiple Aggregations")
print("====================")
print(
    grouped["Python"].agg([
        "mean",
        "max",
        "min",
        "count"
    ])
)


# 9. Create Average column

students["Average"] = students[
    ["Python", "NumPy", "Math"]
].mean(axis=1)

print("\nStudent Averages")
print("====================")
print(
    students[["Student", "Department", "Average"]]
)


# 10. Average student score by Department

print("\nAverage Score By Department")
print("====================")
department_average = students.groupby(
    "Department"
)["Average"].mean()

print(department_average)


# 11. Department with highest average

best_department = department_average.idxmax()

print("\nBest Department")
print("====================")
print("Department:", best_department)
print(
    "Average:",
    department_average[best_department]
)