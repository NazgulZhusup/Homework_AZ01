import pandas as pd

df = pd.read_csv("dz.csv")

df.fillna(0, inplace=True)

print(df)

group = df.groupby("City")['Salary'].mean()

print("Средняя заработная плата по городам:")
print(group)

df = pd.DataFrame(df)

df.to_csv('homework.csv', index=False)
