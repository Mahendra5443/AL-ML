import pandas as pd
df = pd.read_csv("DAY8/students.csv") # df.to_csv("cleaned_students.csv", index=False) for no indexing in df
print(df.iloc[:,0])
print(pd.Shape(df))