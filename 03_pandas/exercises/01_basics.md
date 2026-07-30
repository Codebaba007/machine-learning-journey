# 🏋️ Exercises: Pandas Basics

## Easy (🟢)
1. Create a DataFrame from a dictionary of lists.
2. Read a CSV file into a DataFrame and print the first 5 rows.
3. Select a specific column and calculate its mean.
4. Filter the DataFrame to show only rows where a specific column value is greater than 50.
5. Check for missing values in the entire DataFrame.

## Medium (🟡)
6. Fill all missing values in column 'A' with the mean of column 'A'.
7. Group the data by column 'B' and find the sum of column 'C' for each group.
8. Create a new column 'D' that is the product of columns 'A' and 'B'.
9. Merge two DataFrames on a common column 'ID' using a left join.
10. Set a datetime column as the index and resample the data to monthly frequency, taking the average.

## Hard (🔴)
11. Perform a pivot table operation grouping by two columns and calculating the max and min of a third column.
12. Use `.apply()` with a custom lambda function to normalize a numerical column (min-max scaling).
13. Extract all rows where a string column contains a specific substring, ignoring case.
14. Melt a wide DataFrame into a long format.
15. Optimize the memory of a DataFrame by downcasting float64 to float32 and object to category dtypes.
