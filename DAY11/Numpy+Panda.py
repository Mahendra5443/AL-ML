import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name":["A","B","C","D","E"],
    "Maths":[80,90,70,60,95],
    "Science":[85,88,75,65,92],
    "English":[78,91,72,70,96]
})
df["Total"] = df["Maths"] +df["Science"]+df["English"]
df["Percentage"] = df["Total"]*100/300
df["pass/fail"]=np.where(df["Percentage"]>60,"Pass","Fail")
print(df[df["Total"]==df["Total"].max()]["Total"])
print(df[df["Percentage"]==df["Percentage"].max()]["Percentage"])
print(df[df["Maths"]==df["Maths"].max()]["Maths"])
print(df[df["Science"]==df["Science"].max()]["Science"])
print(df[df["English"]==df["English"].max()]["English"])