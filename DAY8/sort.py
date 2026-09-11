import pandas as py
data={
    "Name":["a","b","c","d"],
    "Grade":["A","C","B","A"],
    "marks":[91,81,70,95]
}
df = py.DataFrame(data)

df = df.sort_values("marks",ascending=False) # or  df.sort_values("marks",ascending=False,inplace=True)

print(df)