import pandas as pd
df1=pd.read_csv("city.csv")
df2=pd.read_csv("expenses.csv")

df=pd.merge(df1,df2,on="city")
print(df)