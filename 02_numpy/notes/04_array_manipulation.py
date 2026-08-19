import numpy as np

array_1 = np.array([1, 2, 3])
array_2 = np.array([5, 6, 7])

combined = np.concatenate((array_1, array_2))

print("Concatenated Array: ",combined)

students_1 = np.array([
    [78, 85, 92],
    [67, 88, 95]
])

students_2 = np.array([
    [72, 81, 89],
    [90, 76, 84]
])

vertical = np.vstack((students_1, students_2))

print("\nVertical Stack: \n", vertical)

horizontal = np.hstack((students_1, students_2))
print("\nVertical Stack: \n", horizontal)

marks = np.array([78, 85, 92])

marks = np.append(marks, 88)

print("\nAfter Append:")
print(marks)

marks = np.array([78, 85, 92])

marks = np.insert(marks, 1, 80)

print("\nAfter Insert:")
print(marks)

marks = np.array([78, 85, 92, 88])

marks = np.delete(marks, 2)

print("\nAfter Delete:")
print(marks)

marks = np.array([78, 45, 92, 38, 88])

result = np.where(marks < 50, 50, marks)

print("\nUsing np.where():")
print(result)

marks = np.array([78, 85, np.nan, 92, 88])

missing = np.isnan(marks)

print("\nMissing Value Detection:")
print(missing)

missing_count = np.sum(np.isnan(marks))

print("\nNumber of Missing Values:")
print(missing_count)
lowest = np.nanmin(marks)
highest = np.nanmax(marks)

print("\nLowest:", lowest)
print("Highest:", highest)
marks = np.array([78, 85, np.nan, 92, 88])

average = np.nanmean(marks)

marks[np.isnan(marks)] = average

print("\nMissing Values Replaced With Average:")
print(marks)


data = np.array([
    [78, 85, 92],
    [67, np.nan, 95],
    [72, 81, 89],
    [np.nan, 76, 84],
    [85, 91, 87]
])
print("\nOriginal Dataset:")
print(data)

print("\nMissing Values:")
print(np.isnan(data))

print("\nMissing Value Count:")
print(np.sum(np.isnan(data)))

column_means = np.nanmean(data, axis=0)

print("\nColumn Means:")
print(column_means)

for column in range(data.shape[1]):
    missing = np.isnan(data[:, column])
    data[missing, column] = column_means[column]

print("\nCleaned Dataset:")