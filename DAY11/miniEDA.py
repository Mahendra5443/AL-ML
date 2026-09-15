import numpy as np
import pandas as pd
df = pd.DataFrame({
    "age":[21,22,23,21,25,26,22,24,100,23],
    "salary":[30000,35000,40000,32000,45000,50000,36000,42000,500000,39000],
    "experience":[1,2,3,1,4,5,2,3,30,3],
    "department":["CSE","ECE","CSE","ME","CSE","ME","CSE","ECE","ME","ECE"]
})

#which value looks suspecious
df["salaryExperienceRatio"]=df["salary"]/df["experience"]
meanOfSalaryExperienceRatio = df["salaryExperienceRatio"].mean()
STDOfSalaryExperienceRatio = df["salaryExperienceRatio"].std()
print(STDOfSalaryExperienceRatio)
print(df.describe())