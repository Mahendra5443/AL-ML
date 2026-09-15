import numpy as np
import pandas as pd

a = pd.DataFrame({
    "name":["a","b","c"],
    "age":[21,22,19],
    "score":[91,95,88]
})
correlation = a["age"].corr(a["score"])
covereience = a["age"].cov(a["score"])

print(a[["age","score"]].corr())
print(a[["age","score"]].cov())
# print(correlation)
# print(covereience)