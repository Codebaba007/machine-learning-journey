# 🚀 Mini Projects: Pandas

## 1. Sales Data Dashboard
**Description:** Load a dataset of retail sales. Clean the data, handle missing values, and extract insights such as top-selling products, monthly revenue trends, and best-performing regions. Output the insights to a clean CSV report.
**Skills:** Datetime handling, `groupby`, aggregations, data cleaning.
**Starter Instructions:** Look for a sample "Superstore Sales" CSV. Convert dates to `pd.to_datetime`. Group by month for revenue.

## 2. COVID-19 Data Explorer
**Description:** Use a public COVID-19 dataset. Calculate the daily new cases and deaths from cumulative data. Find the top 5 countries by total cases, and create a 7-day rolling average of new cases for them.
**Skills:** `.diff()`, `.rolling()`, merging, sorting.
**Starter Instructions:** Use John Hopkins or similar dataset. Use `.diff()` to get daily cases from cumulative counts.

## 3. Student Performance Analyzer
**Description:** Merge multiple CSVs containing student demographics, test scores, and attendance. Clean the merged dataset, create a new feature for "Final Grade", and analyze the correlation between attendance and performance.
**Skills:** `.merge()`, feature engineering, descriptive statistics.
**Starter Instructions:** Create 3 mock CSVs. Merge on `student_id`. Use `.corr()` to check the relationship between attendance and scores.
