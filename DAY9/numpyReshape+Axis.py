import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12]) # a=np.arange(1,13)

a = a.reshape(3,4)

print(a)

# sum of each row
print(a.sum(axis=0))

# sum of each column
print(a.sum(axis=1))

# max of each row
print(a.max(axis=1))

# min of each row
print(a.min(axis=1))

# max of each column
print(a.max(axis=0))

# min of each column
print(a.min(axis=0))