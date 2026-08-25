import pandas as pd

df = pd.read_csv("expenses.csv")
#print(df.describe())

df1=df.groupby("category")["amount"].sum()
df1=df1.sort_values(ascending=False)
print(f"Top spending category: {df1.index[0]} {df1.iloc[0]}")