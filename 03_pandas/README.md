# Pandas

A structured journey through Pandas with a focus on Machine Learning, Data Science, and AI.

---

## Overview

This repository documents my progress as I build a strong foundation in Pandas for Machine Learning.

The goal is to learn Pandas through practical exercises and projects before moving deeper into:

- Matplotlib
- Statistics and Probability
- Scikit-learn
- Machine Learning
- PyTorch
- Deep Learning
- Computer Vision

Every day contains:

- Notes
- Exercises
- A Mini Project


## Day 1 — Pandas Fundamentals

### Topics Covered

- Introduction to Pandas
- Importing Pandas
- Pandas Series
- Pandas DataFrame
- Creating DataFrames
- DataFrame indexes
- Selecting columns
- Selecting multiple columns
- `shape`
- `columns`
- `dtypes`
- `head()`
- `tail()`
- `describe()`
- Calculating column statistics
- Creating calculated columns

### Files

- `notes/01_pandas_fundamentals.py`
- `exercises/exercise_01.py`
- `mini_projects/pandas_student_analyzer.py`

### Learning Outcomes

By the end of this day, I can:

- Understand the purpose of Pandas.
- Create Pandas Series.
- Create Pandas DataFrames.
- Understand rows, columns, and indexes.
- Select individual columns.
- Select multiple columns.
- Inspect the structure of a DataFrame.
- Use `head()` and `tail()` to inspect data.
- Use `describe()` for basic statistical analysis.
- Calculate statistics from DataFrame columns.
- Create new calculated columns.
- Perform basic analysis on structured datasets.

### Mini-Project — Pandas Student Performance Analyzer

Built a student performance analyzer using Pandas.

The project:

- Stores student marks using a Pandas DataFrame.
- Displays the student dataset.
- Displays the dataset shape.
- Displays DataFrame columns.
- Calculates student averages.
- Finds the highest Python mark.
- Finds the highest overall mark.
- Calculates subject averages.
- Identifies the best-performing student.
- Filters students with an average of 80 or higher.

The project introduced Pandas Series, DataFrames, column selection, DataFrame inspection, statistical calculations, and calculated columns.

---


## Day 2 — Data Selection and Filtering

### Topics Covered

- DataFrame row selection
- `loc[]`
- `iloc[]`
- Selecting individual rows
- Selecting multiple rows
- Selecting specific rows and columns
- Boolean filtering
- Conditional filtering
- Multiple conditions
- AND conditions with `&`
- OR conditions with `|`
- Range filtering
- Filtering based on column values
- Selecting columns from filtered data
- Creating calculated columns

### Files

- `notes/02_data_selection.py`
- `exercises/exercise_02.py`
- `mini_projects/pandas_data_filter.py`

### Learning Outcomes

By the end of this day, I can:

- Select rows using `loc[]`.
- Select rows using `iloc[]`.
- Select specific rows and columns.
- Filter DataFrames using Boolean conditions.
- Combine multiple filtering conditions.
- Use `&` for AND conditions.
- Use `|` for OR conditions.
- Filter values within a specific range.
- Select specific columns from filtered data.
- Create calculated columns for further filtering.
- Analyze structured datasets using conditional selection.

### Mini-Project — Pandas Student Data Filter

Built a student data filtering system using Pandas.

The project:

- Stores student marks in a DataFrame.
- Displays selected rows and columns.
- Filters students based on Python marks.
- Filters students based on Mathematics marks.
- Combines multiple conditions using AND.
- Combines multiple conditions using OR.
- Filters marks within a specified range.
- Calculates student averages.
- Identifies students with an average of 80 or higher.

The project combined DataFrame selection, `loc[]`, `iloc[]`, Boolean filtering, multiple conditions, and calculated columns.
---


## Day 3 — Data Cleaning and Missing Values

### Topics Covered

- Missing values
- `isnull()`
- `notnull()`
- `dropna()`
- `fillna()`
- Detecting missing data
- Counting missing values
- Counting non-missing values
- Removing incomplete rows
- Filling missing values
- Filling missing values with column means
- Creating copies of DataFrames with `copy()`
- Cleaning numerical datasets
- Creating calculated columns after cleaning

### Files

- `notes/03_data_cleaning.py`
- `exercises/exercise_03.py`
- `mini_projects/pandas_data_cleaner.py`

### Learning Outcomes

By the end of this day, I can:

- Detect missing values in a DataFrame.
- Count missing values by column.
- Count non-missing values.
- Remove rows containing missing values.
- Replace missing values using `fillna()`.
- Replace missing values with column averages.
- Create a separate working copy using `copy()`.
- Verify that missing values have been removed.
- Create calculated columns after cleaning data.
- Perform basic data-cleaning operations on structured datasets.

### Mini-Project — Pandas Student Data Cleaner

Built a student data cleaning system using Pandas.

The project:

- Stores student marks in a DataFrame.
- Detects missing values.
- Counts missing values by column.
- Displays complete rows using `dropna()`.
- Creates a separate cleaned DataFrame using `copy()`.
- Replaces missing marks with subject averages.
- Verifies the cleaned dataset.
- Calculates student averages.
- Filters high-performing students.
- Identifies the best-performing student.

The project combined missing-value detection, DataFrame cleaning, `copy()`, `fillna()`, statistical calculations, and conditional filtering.

---


## Day 4 — Data Transformation

### Topics Covered

- Creating new columns
- Modifying DataFrame columns
- Calculated columns
- `apply()`
- Lambda functions
- Custom functions
- `map()`
- Renaming columns
- `rename()`
- Sorting DataFrames
- `sort_values()`
- Ascending and descending sorting
- Filtering transformed data
- Data transformation workflows

### Files

- `notes/04_data_transformation.py`
- `exercises/exercise_04.py`
- `mini_projects/pandas_data_transformer.py`

### Learning Outcomes

By the end of this day, I can:

- Create new calculated columns.
- Modify existing DataFrame columns.
- Apply functions to DataFrame values.
- Use lambda functions for simple transformations.
- Create custom functions for data transformation.
- Rename DataFrame columns.
- Sort DataFrames by specific columns.
- Sort values in ascending or descending order.
- Filter transformed DataFrames.
- Combine multiple transformation operations.
- Prepare structured data for further analysis.

### Mini-Project — Pandas Student Data Transformer

Built a student data transformation system using Pandas.

The project:

- Stores student marks in a DataFrame.
- Calculates total marks.
- Calculates student averages.
- Creates pass/fail status.
- Assigns grades using a custom function.
- Renames subject columns.
- Ranks students by average.
- Identifies the best-performing student.
- Filters high-performing students.
- Calculates subject averages.
- Identifies the lowest-performing students.
- Produces a final performance summary.

The project combined calculated columns, `apply()`, lambda functions, custom functions, column renaming, sorting, filtering, and DataFrame transformation.
---

## Day 5 — Grouping and Aggregation

### Topics Covered

- Grouping DataFrames
- `groupby()`
- Group-based analysis
- Group averages
- Group totals
- Group maximum values
- Group minimum values
- Group counts
- `agg()`
- Multiple aggregations
- `idxmax()`
- `nunique()`
- Group-level performance analysis
- Comparing groups using calculated statistics

### Files

- `notes/05_grouping_aggregation.py`
- `exercises/exercise_05.py`
- `mini_projects/pandas_grouped_analyzer.py`

### Learning Outcomes

By the end of this day, I can:

- Group DataFrame data using `groupby()`.
- Calculate averages for individual groups.
- Calculate totals for individual groups.
- Find maximum and minimum values within groups.
- Count records within each group.
- Perform multiple aggregations using `agg()`.
- Find the index of the highest value using `idxmax()`.
- Count unique groups using `nunique()`.
- Compare group-level statistics.
- Analyze performance across different groups.

### Mini-Project — Pandas Grouped Student Analyzer

Built a grouped student performance analyzer using Pandas.

The project:

- Stores student performance data with department information.
- Calculates student averages.
- Groups students by department.
- Counts students in each department.
- Calculates average performance by department.
- Calculates total, highest, and lowest marks by department.
- Performs multiple aggregations.
- Identifies the best-performing department.
- Identifies the best student in each department.
- Calculates the overall class average.
- Finds students performing above the class average.

The project combined `groupby()`, aggregation functions, `agg()`, `idxmax()`, `nunique()`, calculated columns, and group-level analysis.

---

## Day 6 — Data Combining and Merging

### Topics Covered

- Combining DataFrames
- `pd.concat()`
- Combining rows
- Combining columns
- `merge()`
- `join()`
- Merge keys
- `on`
- `left_on`
- `right_on`
- Inner merge
- Left merge
- Right merge
- Outer merge
- Index-based joining
- Combining multiple DataFrames
- Handling missing values after merging

### Files

- `notes/06_combining_merging.py`
- `exercises/exercise_06.py`
- `mini_projects/pandas_data_merger.py`

### Learning Outcomes

By the end of this day, I can:

- Combine DataFrames using `concat()`.
- Combine DataFrames vertically and horizontally.
- Merge DataFrames using common keys.
- Use different merge types.
- Understand inner, left, right, and outer merges.
- Merge DataFrames with differently named key columns.
- Join DataFrames using their indexes.
- Understand the difference between `concat()`, `merge()`, and `join()`.
- Combine multiple datasets into a single DataFrame.
- Handle missing values created during data merging.

### Mini-Project — Pandas Student Data Merger

Built a student data merging system using Pandas.

The project:

- Stores student information separately from marks and attendance.
- Combines datasets using `merge()`.
- Demonstrates inner and left merges.
- Adds attendance information to the main dataset.
- Handles missing marks.
- Calculates student averages.
- Filters high-performing students.
- Filters students based on attendance.
- Performs department-level analysis.
- Identifies the best-performing student.
- Produces a final combined dataset.

The project combined `merge()`, multiple DataFrames, missing-value handling, calculated columns, filtering, and `groupby()` analysis.
---


## Day 7 — Data Input and Output

### Topics Covered

- Reading CSV files
- Writing CSV files
- `read_csv()`
- `to_csv()`
- Reading Excel files
- Writing Excel files
- `read_excel()`
- `to_excel()`
- Reading JSON files
- Writing JSON files
- `read_json()`
- `to_json()`
- `usecols`
- Dataset inspection
- Loading and saving real data
- DataFrame ↔ file workflows

### Files

- `notes/07_data_io.py`
- `exercises/exercise_07.py`
- `mini_projects/pandas_file_analyzer.py`

### Learning Outcomes

By the end of this day, I can:

- Load CSV data into a DataFrame.
- Save DataFrames as CSV files.
- Load and save Excel files.
- Load and save JSON files.
- Select specific columns while importing data.
- Inspect imported datasets.
- Build a basic file-based data pipeline.
- Clean and transform imported data.
- Export processed datasets.

### Mini-Project — Pandas Student File Analyzer

Built a student file analysis system using Pandas.

The project:

- Loads student data from a CSV file.
- Inspects the dataset structure.
- Checks for missing values.
- Cleans missing numerical values.
- Calculates total and average marks.
- Assigns grades.
- Determines pass/fail status.
- Sorts students by performance.
- Identifies top students.
- Calculates class statistics.
- Creates a grade distribution.
- Exports the analyzed dataset.
- Exports the top-performing students.

The project combined file I/O, DataFrame inspection, data cleaning, transformation, analysis, and exporting results.
---


## Day 8 — Data Cleaning and Preprocessing

### Topics Covered

- Duplicate detection
- `duplicated()`
- `drop_duplicates()`
- Cleaning column names
- String cleaning
- `.str.strip()`
- Standardizing text values
- `.str.lower()`
- `replace()`
- Data type conversion
- `astype()`
- `pd.to_numeric()`
- Handling invalid numeric values
- Missing-value preprocessing
- Filling missing values
- Creating calculated columns
- Data preprocessing pipelines
- Exporting cleaned datasets

### Files

- `notes/08_data_preprocessing.py`
- `exercises/exercise_08.py`
- `mini_projects/pandas_preprocessing_pipeline.py`

### Learning Outcomes

By the end of this day, I can:

- Detect duplicate rows.
- Remove duplicate records.
- Clean whitespace from column names and text values.
- Standardize inconsistent text values.
- Convert string-based numerical data into numeric data.
- Handle invalid numerical values.
- Detect and handle missing values.
- Create calculated columns after preprocessing.
- Build a basic data preprocessing pipeline.
- Export a cleaned dataset for further analysis or machine learning.

### Mini-Project — Pandas Student Data Preprocessing Pipeline

Built a complete student data preprocessing pipeline using Pandas.

The project:

- Starts with intentionally messy student data.
- Cleans column names.
- Removes duplicate records.
- Cleans student names.
- Converts score columns into numeric values.
- Detects missing values.
- Fills missing scores using column means.
- Standardizes status values.
- Renames score columns.
- Calculates total and average marks.
- Assigns student grades.
- Sorts students by performance.
- Identifies high-performing students.
- Performs final data-quality checks.
- Exports the cleaned dataset as a CSV file.

The project combined duplicate handling, string cleaning, type conversion, missing-value handling, value standardization, feature creation, filtering, sorting, and file export into a practical preprocessing pipeline.

---

## Day 9 — Data Analysis and Descriptive Statistics

### Topics Covered

- Descriptive statistics
- `describe()`
- `mean()`
- `median()`
- `mode()`
- `std()`
- `var()`
- `min()`
- `max()`
- `sum()`
- `count()`
- `quantile()`
- `corr()`
- Statistical summaries
- Data distribution
- Performance comparison
- Correlation analysis

### Files

- `notes/09_descriptive_statistics.py`
- `exercises/exercise_09.py`
- `mini_projects/pandas_statistics_analyzer.py`

### Learning Outcomes

By the end of this day, I can:

- Generate descriptive statistical summaries.
- Calculate mean, median, and mode.
- Calculate standard deviation and variance.
- Find minimum and maximum values.
- Calculate totals and counts.
- Calculate quartiles using `quantile()`.
- Analyze relationships between numerical columns using correlation.
- Compare subject-level statistics.
- Analyze student performance using statistical measures.
- Use Pandas for basic exploratory data analysis.

### Mini-Project — Pandas Student Statistics Analyzer

Built a student statistics analysis system using Pandas.

The project:

- Analyzes student performance across multiple subjects.
- Generates descriptive statistics.
- Calculates subject means, medians, and modes.
- Measures standard deviation and variance.
- Calculates quartiles.
- Analyzes correlations between subjects.
- Compares subject averages.
- Calculates individual student averages.
- Identifies the best and lowest-performing students.
- Finds students above the class average.
- Measures performance ranges.
- Produces a final statistical summary.

The project combined Pandas statistical functions with practical student-performance analysis.

---


## Day 10 — Pivot Tables and Advanced Analysis

### Topics Covered

- `value_counts()`
- `pivot_table()`
- `crosstab()`
- `melt()`
- `pivot()`
- Multi-level analysis
- Department-level analysis
- Gender-based analysis
- Wide and long data formats
- Data reshaping
- Group-based statistical analysis

### Files

- `notes/10_pivot_tables.py`
- `exercises/exercise_10.py`
- `mini_projects/pandas_pivot_analyzer.py`

### Learning Outcomes

By the end of this day, I can:

- Count categorical values using `value_counts()`.
- Create summary tables using `pivot_table()`.
- Analyze data across multiple categories.
- Create frequency tables using `crosstab()`.
- Calculate category percentages.
- Convert wide data into long format using `melt()`.
- Convert long data back into wide format using `pivot()`.
- Perform multi-dimensional DataFrame analysis.
- Compare performance across departments and genders.
- Reshape datasets for analysis and visualization.

### Mini-Project — Pandas Student Performance Pivot Analyzer

Built an advanced student performance analysis system using Pandas.

The project:

- Analyzes student distribution by department and gender.
- Creates department-level performance summaries.
- Compares subject performance across departments.
- Performs department and gender analysis.
- Generates categorical frequency tables.
- Calculates department-wise gender percentages.
- Reshapes student data from wide to long format.
- Analyzes average performance by subject.
- Identifies the best-performing subject.
- Converts long-format data back to wide format.
- Identifies the best student in each department.
- Produces a final performance summary.

The project combined `value_counts()`, `pivot_table()`, `crosstab()`, `melt()`, `pivot()`, `groupby()`, and statistical analysis.
---

## Day 11 — Working with Dates and Time

### Topics Covered

- `pd.to_datetime()`
- Datetime conversion
- `.dt` accessor
- Extracting year, month, and day
- `month_name()`
- `day_name()`
- Date differences
- Date filtering
- Date sorting
- `pd.date_range()`
- Time-based data analysis

### Files

- `notes/11_datetime.py`
- `exercises/exercise_11.py`
- `mini_projects/pandas_date_analyzer.py`

### Learning Outcomes

By the end of this day, I can:

- Convert string dates into Pandas datetime values.
- Extract useful information from dates.
- Find weekdays and month names from dates.
- Calculate the number of days between dates.
- Filter DataFrames using dates.
- Sort records chronologically.
- Generate date ranges.
- Perform basic time-based data analysis.

### Mini-Project — Pandas Student Date Analyzer

Built a student date analysis system using Pandas.

The project:

- Converts student join and exam dates into datetime values.
- Extracts year, month, day, and weekday information.
- Calculates preparation time between dates.
- Filters students by join date.
- Identifies students with longer preparation periods.
- Creates a monthly student distribution.
- Builds an exam schedule.
- Identifies the highest-performing student.
- Exports the analyzed date dataset.

The project combined datetime conversion, `.dt` operations, date arithmetic, filtering, sorting, and file export.
---

## Day 12 — Working with Text Data

### Topics Covered

- `.str` accessor
- `.str.lower()`
- `.str.upper()`
- `.str.strip()`
- `.str.replace()`
- `.str.contains()`
- `.str.startswith()`
- `.str.endswith()`
- `.str.len()`
- `.str.split()`
- `.str.extract()`
- Combining string operations
- Text cleaning and preprocessing

### Files

- `notes/12_text_data.py`
- `exercises/exercise_12.py`
- `mini_projects/pandas_text_analyzer.py`

### Learning Outcomes

By the end of this day, I can:

- Perform string operations on Pandas columns.
- Standardize text using lowercase, uppercase, and title case.
- Remove unnecessary spaces.
- Replace specific text values.
- Search and filter text using patterns.
- Check whether text starts or ends with specific values.
- Measure string length.
- Split text into separate parts.
- Extract patterns from text.
- Combine multiple string operations for data cleaning.

### Mini-Project — Pandas Text Analyzer

Built a text analysis and preprocessing system using Pandas.

The project:

- Cleans student names, departments, and statuses.
- Standardizes inconsistent text.
- Extracts email usernames and domains.
- Calculates name lengths.
- Filters students by email and department.
- Searches names for specific text.
- Identifies active students.
- Counts students by department and email domain.
- Finds the student with the longest name.
- Exports the cleaned dataset to CSV.

The project combined Pandas string operations with filtering, extraction, aggregation, and data preprocessing.

---

## Day 13 — Working with Categorical Data

### Topics Covered

- Categorical data
- `astype("category")`
- `.cat.categories`
- `.cat.codes`
- `.cat.rename_categories()`
- `.cat.add_categories()`
- `.cat.remove_categories()`
- `.cat.set_categories()`
- Ordered categorical data
- `.cat.reorder_categories()`
- `value_counts()`
- Filtering categorical data
- Sorting categorical data
- Categorical data analysis

### Files

- `notes/13_categorical_data.py`
- `exercises/exercise_13.py`
- `mini_projects/pandas_category_analyzer.py`

### Learning Outcomes

By the end of this day, I can:

- Identify categorical data in a DataFrame.
- Convert columns to the categorical data type.
- View categories and their numerical codes.
- Add, remove, rename, and set categories.
- Create ordered categorical data.
- Reorder categories.
- Filter and sort categorical data.
- Analyze categorical distributions.
- Use categorical data for practical preprocessing.

### Mini-Project — Pandas Categorical Data Analyzer

Built a categorical data analysis system using Pandas.

The project:

- Converts student columns into categorical data.
- Inspects categories and category codes.
- Adds and removes categories.
- Renames existing categories.
- Creates ordered performance categories.
- Counts students by department and performance.
- Filters students based on performance.
- Sorts students using ordered categories.
- Analyzes departments and performance using a cross-tabulation.
- Exports the analyzed dataset to CSV.

The project combined categorical data types, category management, ordering, filtering, sorting, and categorical analysis.

### Current Progress

Pandas — Day 13 completed — Covered categorical data, category management, ordered categories, filtering, sorting, and categorical analysis.

Next Step: Continue with Pandas Day 14 and complete the remaining practical Pandas topics before moving to Matplotlib and Statistics.

## Repository Structure

```text
03_pandas/
│
├── README.md
│
├── notes/
│   └── 01_pandas_fundamentals.py
│
├── exercises/
│   └── exercise_01.py
│
└── mini_projects/
    └── pandas_student_analyzer.py