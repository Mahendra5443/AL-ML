import pandas as pd
df = pd.DataFrame({
    "department": ["CSE","CSE","ECE","ECE","ME","ME","CSE"],
    "employee": ["A","B","C","D","E","F","G"],
    "salary": [50000,60000,45000,55000,40000,48000,70000]
})
# Average salary per department
# Maximum salary per department
# Minimum salary per department
# Number of employees per department
# Which department has the highest average salary?
data = pd.DataFrame(df)
print(data.groupby(["department"])["salary"].max())
print(data.groupby(["department"])["salary"].mean())
print(data.groupby(["department"])["salary"].min())
print(data.groupby(["department"])["employee"].count())
# print(data[data["salary"] == data["salary"].max()]["department"]) or
print(data[data["salary"] == data["salary"].max()][["department"]])