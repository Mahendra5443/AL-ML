import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])

temp = np.where(a>5) # gets array of X-axis and Y-axis 
moreThen5 = a[temp] #gets array of values that passes condition 
print(moreThen5.sum()) # gets sum of all elements