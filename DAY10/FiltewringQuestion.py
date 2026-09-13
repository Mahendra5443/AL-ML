import numpy as np
import pandas as pd

df = pd.DataFrame({
    "name" :["A","B","C","D"],
    "age" :[28,22,21,24],
    "marks" :[85,92,67,55],
    "city" :["U","J","U","D"]
})

print(df.where(df["marks"]>60)[["name","marks"]]) # or
print(df[df["marks"]>60][["name","marks"]]) # or
print(df.loc[df["marks"]>60,["name","marks"]])