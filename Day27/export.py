import pandas as pd
df = pd.read_csv("expenses.csv")
df["amount_usd"]=df["amount"]/83
df.to_csv("expenses_usd.csv",index=False)
