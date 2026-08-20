import numpy as np

np.random.seed(42)

# 1. Generate 10 random integers between 1 and 100
numbers = np.random.randint(1, 101, size=10)
print("Numbers:", numbers)

# 2. Calculate statistics
print("Average:", np.mean(numbers))
print("Highest:", np.max(numbers))
print("Lowest:", np.min(numbers))
print("Standard Deviation:", np.std(numbers))

# 3. Generate a 5x3 marks dataset
marks = np.random.randint(40, 101, size=(5, 3))
print("\nMarks:")
print(marks)

# 4. Subject averages
print("\nSubject Averages:")
print(np.mean(marks, axis=0))

# 5. Student averages
print("\nStudent Averages:")
print(np.mean(marks, axis=1))

# 6. Generate 100 heights using normal distribution
heights = np.random.normal(170, 8, size=100)

print("\nHeight Average:", np.mean(heights))
print("Height Std:", np.std(heights))

# Challenge: students with average >= 80
student_averages = np.mean(marks, axis=1)

print("\nStudents >= 80:")
print(np.where(student_averages >= 80)[0] + 1)