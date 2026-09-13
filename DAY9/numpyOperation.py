import numpy as np

a = np.array([[1,2,3,4]])

print(a.sum())

print(a.min())

print(a.mean())

print(a.max())
#standerd Daviation
print(np.std(a))
#median
print(np.median(a))

print(a[a>a.mean()])

print(a[a%2==0])