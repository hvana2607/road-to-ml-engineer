import pandas as pd
df = pd.DataFrame({"name":["A","B"],"age":[30,40]})
#print(df)
print(df[df["age"]>30])