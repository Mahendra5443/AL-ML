import numpy as np
import pandas as pd
a = np.array([
    [101,85,20],
    [102,72,21],
    [103,91,19],
    [104,78,20]
])

data=pd.DataFrame(a,columns=["student_id","marks","age"])

#Average of marks
print(data["marks"].mean())

#Average of marks
print(data["marks"].max())

#student ID of student having maximum marks
print(data.loc[data["marks"].idxmax(),"student_id"]) # or data[data["marks"]==data["marks"].max()]
print(data[data["marks"]==data["marks"].max()]["student_id"])

#sort by makrs
print(data.sort_values("marks",ascending=False))