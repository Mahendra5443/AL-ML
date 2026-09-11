import pandas as pd
data = {
    "department": ["CSE", "CSE", "ECE", "ECE", "CSE", "ME"],
    "name": ["A", "B", "C", "D", "E", "F"],
    "marks": [85, 62, 91, 48, 76, 88]
}

df = pd.DataFrame(data)
newData = df[df["marks"]>50] # & for and | for or
df["percantage"]=df["marks"]*100/100
print(newData)
print(df)