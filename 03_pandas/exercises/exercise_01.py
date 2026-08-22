import pandas as pd

data = {
    "Python": [78, 67, 72, 90, 85],
    "NumPy": [85, 88, 81, 76, 91],
    "Math": [92, 95, 89, 84, 87]
}

df = pd.DataFrame(data)

print("Pandas DataFrame: \n", df)
print("\nPython marks: \n", df["Python"])
print("\nNumPy marks: \n", df["NumPy"])
print("\nMath marks: \n", df["Math"])
print("\nShape of DataFrame: ", df.shape)
print("\nColumns names: ", df.columns)
print("\nData types: ", df.dtypes)
print("\nFirst 3 rows of DataFrame: \n", df.head(3))
print("\nLast 3 rows of DataFrame: \n", df.tail(3))
print("\ndataset satatistics: \n", df.describe())
print("\nAverage of the python marks: ", df["Python"].mean())