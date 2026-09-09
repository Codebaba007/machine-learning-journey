import pandas as pd

students_a = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Department": ["CSE", "EEE", "CSE"]
})

students_b = pd.DataFrame({
    "Student_ID": [4, 5, 6],
    "Name": ["David", "Emma", "Frank"],
    "Department": ["BBA", "EEE", "CSE"]
})

scores = pd.DataFrame({
    "Student_ID": [1, 2, 3, 5, 6],
    "Math": [85, 72, 91, 78, 88],
    "Python": [90, 68, 95, 82, 92]
})

all_students = pd.concat(
    [students_a, students_b],
    ignore_index=True
)

student_scores = pd.merge(
    all_students,
    scores,
    on="Student_ID",
    how="left"
)

student_scores["Math"] = student_scores["Math"].fillna(0)
student_scores["Python"] = student_scores["Python"].fillna(0)

student_scores["Average"] = (
    student_scores["Math"] + student_scores["Python"]
) / 2

top_students = student_scores.nlargest(
    3,
    "Average"
)

print("All Students")
print(all_students)

print("\nCombined Student Scores")
print(student_scores)

print("\nTop 3 Students")
print(top_students)