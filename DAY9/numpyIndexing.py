import numpy as np

a = np.array([
    [10,20,30,40,50],
    [60,70,80,90,100],
    [110,120,130,140,150]
])
# print a element
print(a[1,1])
# print slice of a row or column
print(a[0,1:4]) #or use print(a[(a>=20) & (a<=40)])
# print last row or column
print(a[-1,:])
print(a[:,-1])
# print last 2 row
print(a[a.shape[0]-2:a.shape[0],:]) # or 
print(a[-2:,:])