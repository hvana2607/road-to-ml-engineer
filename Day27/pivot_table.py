import pandas as pd

df = pd.read_csv("expenses.csv")

df=df.pivot_table(index="city",columns="category",values="amount",aggfunc="sum")
print(df)