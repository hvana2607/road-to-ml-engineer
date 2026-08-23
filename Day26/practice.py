import pandas as pd
df3=pd.read_csv("test.csv")
#print(df3.head())
#print(df3["age"])
df3["senior"] = df3["age"] > 35
#print(df3)
df3 = df3.sort_values("age",ascending=False)
print(df3)