# in [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print 5
# print shape of it
# print last column
# print last raw
# sum of each raw
# sum of each column
import numpy as np
a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(a[1,1]) # print(a[size[0]/2],a[size[1]/2])
size = (a.shape)
print(a[size[0]/2],a[size[1]/2])
print(size)
