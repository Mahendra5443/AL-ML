import numpy as np
import pandas as pd

a = np.arange(1,10).reshape(3,3)
data = pd.DataFrame(a,columns=["student_id", "marks", "age"])

print(data)

print(data["marks"].mean())

print(data[data["marks"] == data["marks"].max()]["student_id"])

print(data[data["marks"]>=5]["student_id"])

print(data.sort_values(by="marks",ascending=False))

print(data)