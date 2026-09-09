import numpy as np

number1 = np.array([1,2,3,4,5])
print(number1.shape)
print(number1.dtype)
number2 = np.array([1,2,3,4,5])
print(number1+number2)
print(number1*2)
print(number1[0])
print(number1[-1])
print(number1[1:4])
number3 = np.array([[1],[2],[3],[4],[5]])
print(number3.shape)