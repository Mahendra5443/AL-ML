# for data = {
#     "department": ["CSE", "CSE", "ECE", "ECE", "CSE", "ME"],
#     "name": ["A", "B", "C", "D", "E", "F"],
#     "marks": [85, 62, 91, 48, 76, 88]
# }
# 1.Which student has the highest marks?
# 2.Average marks of each department?
# 3.Highest marks in each department?
# 4.How many students are in each department?
# 5.Show students with marks > 75, sorted from highest to lowest.
# 6.Add a grade column:
# 90+     → A
# 80–89   → B
# 70–79   → C
# 60–69   → D
# <60     → F without loop
import pandas as pd
data = {
    "department": ["CSE", "CSE", "ECE", "ECE", "CSE", "ME"],
    "name": ["A", "B", "C", "D", "E", "F"],
    "marks": [85, 62, 91, 48, 76, 88]
}

df = pd.DataFrame(data)
print(df[["name","department"]])

