import pandas as pd
data = {
    "department": ["CSE", "CSE", "ECE", "ECE", "CSE", "ME"],
    "name": ["A", "B", "C", "D", "E", "F"],
    "marks": [85, 62, 91, 48, 76, 88]
}

df = pd.DataFrame(data)
print(df[["name","department"]])
