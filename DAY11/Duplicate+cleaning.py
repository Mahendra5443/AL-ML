import pandas as pd
import numpy as np
df = pd.DataFrame({
    "id": [1,2,2,3,4,4,5],
    "name": ["A","B","B","C","D","D","E"],
    "marks": [80,90,90,70,None,85,95]
})
# Create a clean DataFrame where:
# Duplicate records are identified.
# Duplicates are removed.
# Missing marks are handled.
# Index is reset.
# Final DataFrame contains no missing values or duplicate rows.
# Then explain:
# Why should you inspect duplicates before simply deleting them?

# duplicateData = df.groupby("name").value_counts().sum()>1
# print(duplicateData)
cleanData = df.drop_duplicates()
# print(cleanData)

#  = cleanData.where([cleanData["marks"]==None],cleanData["marks"].mean(),)
meanV = cleanData["marks"].mean()
cleanData["marks"] = np.where(cleanData["marks"].isna(), meanV,cleanData["marks"])
print(cleanData)

#index is reset
