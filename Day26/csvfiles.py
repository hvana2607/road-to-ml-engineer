import pandas as pd
df2=pd.read_csv("test.csv")
#print(df2.head())
#print(df2.groupby("city").size())
print(df2.groupby("city")["age"].mean())