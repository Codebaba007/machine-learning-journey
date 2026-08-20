import numpy as np


# ============================================================
# Random Student Dataset Generator
# ============================================================

np.random.seed(42)

students = 20
subjects = ["Python", "NumPy", "Mathematics"]

marks = np.random.randint(
    40,
    101,
    size=(students, len(subjects))
)

print("RANDOM STUDENT DATASET")
print("============================")

print("\nDataset:")
print(marks)

print("\nDataset Shape:", marks.shape)


# Subject statistics

subject_averages = np.mean(marks, axis=0)
subject_highest = np.max(marks, axis=0)
subject_lowest = np.min(marks, axis=0)

print("\nSubject Statistics")
print("----------------------------")

for i in range(len(subjects)):
    print(f"\n{subjects[i]}")
    print("Average:", subject_averages[i])
    print("Highest:", subject_highest[i])
    print("Lowest:", subject_lowest[i])


# Student statistics

student_averages = np.mean(marks, axis=1)

print("\nStudent Averages")
print("----------------------------")

for i in range(students):
    print(f"Student {i + 1}: {student_averages[i]:.2f}")


# Performance

best_student = np.argmax(student_averages)
worst_student = np.argmin(student_averages)

print("\nPerformance")
print("----------------------------")
print("Best Student:", best_student + 1)
print("Best Average:", student_averages[best_student])

print("Lowest Student:", worst_student + 1)
print("Lowest Average:", student_averages[worst_student])


# Overall statistics

print("\nOverall Statistics")
print("----------------------------")
print("Overall Average:", np.mean(marks))
print("Highest Mark:", np.max(marks))
print("Lowest Mark:", np.min(marks))
print("Standard Deviation:", np.std(marks))


# Pass/fail

passed = student_averages >= 50

print("\nPass/Fail")
print("----------------------------")
print("Passed:", np.sum(passed))
print("Failed:", np.sum(~passed))


# Reproducibility

print("\nRandom Seed: 42")
print("Dataset can be reproduced exactly.")