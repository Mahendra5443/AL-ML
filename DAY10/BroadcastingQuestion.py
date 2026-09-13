# Different tax rates apply to each column:Use broadcasting to calculate the final prices.

import numpy as np
import pandas as pd
a= np.arange(1, 13).reshape(3,4)
print(a)
#applying rates to column
rate = [1,2,4,8]
print(a*rate)

#applying rates to row
print(a*[[2],[4],[8]])

#applying rates to column and row both

print(a*rate*[[2],[4],[8]])