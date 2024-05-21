import pandas as pd

df = pd.read_csv("data_scientists_salaries_from_reddit.csv")

print(df.head())
print(df.info())
print(df.describe())