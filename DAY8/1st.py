import pandas as pd

data = {
    "name" : ["raj","shyam", "rita"],
    "age" : [22,21,19],
     "marks": [85, 72, 91]
}
pandadata = pd.DataFrame(data)

# print(pandadata.head())
# print()
# print(pandadata.tail())
# print()
# print(pandadata.columns)
# print()
# print(pandadata.shape) # 3 rows, 3 columns.
# print()
# print(pandadata.info())
# print()
# print(pandadata.describe()) # gives statistical summaries of numerical columns.

# print(pandadata["name"]) # print name column 1-D array

# print(pandadata[["marks"]]) # print marks column 2-D array and multiple column array

# print(pandadata[["name", "marks"]]) # print name and marks column

# print(pandadata.loc[0]) # print first ROW

# print(pandadata.loc[0:1]) # print column till index 1

# print(pandadata.iloc[0]) # print first row

# print(pandadata.iloc[0:2]) # print row till index 1G?