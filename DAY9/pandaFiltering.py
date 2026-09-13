import numpy as np
import pandas as pd

data = {
    "name": ["a", "b", "c", "d", "e", "f"],
    "age": [20, 22, 21, 24, 19, 18],
    "marks": [85, 67, 92, 88, 87, 81],
    "city": ["U", "J", "D", "B", "U", "U"],
}

df = pd.DataFrame(data)

# 1. Filtering condition
print(df[(df["marks"] > 80) & (df["city"] == "U")])

# 2. Binary classification using np.where
df["passed"] = np.where(df["marks"] > 85, "passed", "fail")

# 3. Multi-condition grading using np.select
conditions = [
    df["marks"] >= 90,
    df["marks"] >= 80,
    df["marks"] >= 70,
    df["marks"] >= 60,
]
choices = ["A", "B", "C", "D"]

df["grade"] = np.select(conditions, choices, default="E")

print(df)