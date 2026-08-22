import pandas as pd

marks = pd.Series([79, 85, 92, 67, 88])

print("Pandas Series: \n", marks)

print("\nFirst Mark: ", marks[0])

data = {
    "Python": [85, 90, 78, 92],
    "Numpy": [88, 76, 95, 89],
    "maths": [90, 85, 88, 92]
}
df = pd.DataFrame(data)

print("\nPandas DataFrame: \n", df)

print("\nPython Marks: \n", df["Python"])

print("\nShape of DataFrame: ", df.shape)

print("\ncolumns of DataFrame: ", df.columns)

print("\nData types of DataFrame: ", df.dtypes)

print("\nfirst row of DataFrame: \n", df.head())
print("\nlast row of DataFrame: \n", df.tail())

print("\nDataset Statistics: \n", df.describe())