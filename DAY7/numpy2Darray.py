import numpy as np
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [11,12,13]
])
print(a) #0 indexing in 2 d array
print(a.shape)
a = a.reshape(2,6)
print(a)
print(a.shape)

print(a.sum())
print(a.mean())
print(a.min())
print(a.max())