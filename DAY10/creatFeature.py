import numpy as np
import pandas as pd

data = pd.DataFrame({
    "name":["A","B","C"],
    "age":[20,22,21],
    "marks":[85,67,92]
})
print(data)
data["passed"] = np.where(data["marks"]>80,"pass","fail")
print(data)

conditions =[
    data["marks"]>90,
    data["marks"]>80,
    data["marks"]>70,
    data["marks"]>60,
]
grade =["A","B","C","D"]

data["grade"] = np.select(conditions,grade,default="E")
print(data)