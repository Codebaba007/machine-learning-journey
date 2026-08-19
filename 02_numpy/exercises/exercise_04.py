import numpy as np

marks = np.array([
    [78, 85, 92],
    [67, np.nan, 95],
    [72, 81, 89],
    [np.nan, 76, 84],
    [85, 91, 87]
])

# 1. Shape
print("Shape:", marks.shape)

# 2. Total missing values
print("Missing Values:", np.sum(np.isnan(marks)))

# 3. Subject averages ignoring missing values
subject_averages = np.nanmean(marks, axis=0)
print("Subject Averages:", subject_averages)

# 4. Replace missing values with subject average
for column in range(marks.shape[1]):
    missing = np.isnan(marks[:, column])
    marks[missing, column] = subject_averages[column]

# 5. Cleaned dataset
print("\nCleaned Dataset:")
print(marks)

# 6. Student averages
student_averages = np.mean(marks, axis=1)
print("\nStudent Averages:")
print(student_averages)

# 7. Highest mark in each subject
highest_by_subject = np.max(marks, axis=0)
print("\nHighest By Subject:")
print(highest_by_subject)

# 8. Students with average >= 80
high_performers = np.where(student_averages >= 80)[0] + 1
print("\nStudents With Average >= 80:")
print(high_performers)

# 9. Sort each student's marks
sorted_marks = np.sort(marks, axis=1)
print("\nSorted Student Marks:")
print(sorted_marks)

# 10. Add another student
new_student = np.array([[90, 88, 94]])

marks = np.vstack((marks, new_student))

print("\nAfter Adding New Student:")
print(marks)

# Challenge: best student
student_averages = np.mean(marks, axis=1)
best_student = np.argmax(student_averages)

print("\nBest Student:", best_student + 1)
print("Average:", student_averages[best_student])