import numpy as np
import pandas as pd
df = pd.DataFrame({
    "age":[21,22,23,21,25,26,22,24,100,23],
    "salary":[30000,35000,40000,32000,45000,50000,36000,42000,500000,39000],
    "experience":[1,2,3,1,4,5,2,3,30,3],
    "department":["CSE","ECE","CSE","ME","CSE","ME","CSE","ECE","ME","ECE"]
})

numaricColumn = ["age","experience","salary"]
Q1 = np.percentile(df[numaricColumn], 25) # or Q1 = df[numeric_cols].quantile(0.25)
Q2 = np.percentile(df[numaricColumn], 50) # df[numeric_cols].quantile(0.50)
Q3 = np.percentile(df[numaricColumn], 75) # df[numeric_cols].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df[numaricColumn] > (Q3 + 1.5 * IQR)).any(axis=1)]

print(outliers)

df = df.drop(index = outliers.index)
print(df)
print(df.describe())