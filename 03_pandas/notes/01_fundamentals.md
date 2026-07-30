# 📝 Notes: Pandas Fundamentals

## 1. DataFrames & Series
- **Series**: A 1D labeled array capable of holding any data type.
- **DataFrame**: A 2D labeled data structure with columns of potentially different types (like a SQL table or Excel spreadsheet).

## 2. Selection and Indexing
- `df['col']`: Selects a column (returns a Series).
- `df.loc[]`: Label-based indexing. E.g., `df.loc[row_label, col_label]`.
- `df.iloc[]`: Integer/position-based indexing. E.g., `df.iloc[0, 1]`.
- Boolean indexing: `df[df['age'] > 30]` filters rows.

## 3. Data Cleaning
Data is rarely clean. Handling nulls is critical:
- `.isnull().sum()` identifies missing values.
- `.dropna()` removes rows/columns with nulls.
- `.fillna(val)` imputes missing values (e.g., with mean or median).

## 4. GroupBy
The split-apply-combine paradigm:
1. **Split** data into groups based on some criteria.
2. **Apply** a function to each group independently (e.g., sum, mean).
3. **Combine** the results into a data structure.
`df.groupby('category').mean()`

## 5. Merging & Concatenation
- `.concat([df1, df2])`: Glues DataFrames together (vertically or horizontally).
- `.merge(df1, df2, on='key')`: Database-style joins (inner, outer, left, right).
