# 🐼 Pandas Cheatsheet

```python
import pandas as pd
```

## Series & DataFrame Creation
```python
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
```

## Reading/Writing Data
```python
df = pd.read_csv('data.csv')
df.to_csv('out.csv', index=False)
pd.read_excel('data.xlsx')
pd.read_json('data.json')
```

## Selecting Data
```python
df['A'] # Column
df.loc[0, 'A'] # Label-based
df.iloc[0, 1] # Integer-based
df[df['A'] > 5] # Boolean indexing
```

## Data Cleaning
```python
df.dropna() # Drop missing values
df.fillna(0) # Fill missing values
df.drop_duplicates()
df.dtypes
df['A'] = df['A'].astype('int32')
```

## Data Transformation
```python
df['A'].apply(lambda x: x*2)
df['B'].map({'cat': 1, 'dog': 0})
df.replace(0, np.nan)
df.rename(columns={'A': 'new_A'})
```

## Groupby & Aggregation
```python
df.groupby('category').mean()
df.groupby('category').agg({'A': 'sum', 'B': 'max'})
```

## Merging & Joining
```python
pd.merge(df1, df2, on='id', how='left')
pd.concat([df1, df2], axis=0) # Vertically
```

## Pivot Tables & Crosstab
```python
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
pd.crosstab(df['A'], df['B'])
```

## Time Series Basics
```python
pd.to_datetime(df['date'])
df.set_index('date').resample('M').mean()
```

## String Methods
```python
df['name'].str.lower()
df['name'].str.contains('John')
```

## Categorical Data
```python
df['cat'] = df['cat'].astype('category')
```

## Memory Optimization Tips
- Downcast numeric types (e.g., float64 to float32).
- Use `category` dtype for columns with few unique values.
