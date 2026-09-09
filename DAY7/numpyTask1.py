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
]) # np.arange(1, 10)
b = np.arange(1, 10)
b =b.reshape(3,3)
print(b)
print(a[1,1]) # or print(a[int(size[0]/2),int(size[1]/2)])
size = (a.shape)
print(a[int(size[0]/2),int(size[1]/2)])

print(size)
print(a[:,-1])  # print last column
print(a[-1,:])  # print last raw
print(np.sum(a,axis=0))  # sum of along raw
print(np.sum(a,axis=1))  # sum of along column