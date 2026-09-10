import pandas as pd

FILE_PATH = "data/US_Accidents_March23.csv"

df = pd.read_csv(FILE_PATH, nrows=10000)

print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
print(df.head())
print(df.isnull().sum().sort_values(ascending=False))