import pandas as pd

data={
    "name": ["A","B","C","D"],
    "marks": [70,95,81,91],
    "age": [23,19,18,21],
    "grade": ["C","A","B","A"],
    "department": ["CSE", "CSE", "CSE", "ECE"]
}

df = pd.DataFrame(data)

print(df.groupby("department")["marks"].mean())