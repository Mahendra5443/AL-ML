import numpy as np

a = np.array([
    [100,200,300],
    [400,500,600],
    [700,800,900],
])

# apply different rate for different row
b = [
  [1.05],
  [1.1],
  [1.2]
 ]
result1 = (a*b).astype(int) # conver to int
print(result1)

# apply different rate for different column
c =[1.05,1.1,1.2]
result2 = (a*c).astype(int) # conver to int
print(result2)