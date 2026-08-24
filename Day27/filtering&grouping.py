import pandas as pd

df = pd.read_csv("expenses.csv")
#df1=df[(df["amount"] >100) & (df["category"] == "food")]
# df1=df.groupby("category")["amount"].sum()
df1=df.groupby(["category","city"])["amount"].sum()
print(df1)
