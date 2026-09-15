from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
iris = load_iris()
# X = np.arange(1,11).reshape(5,2)
X = iris.data
# Y = np.array([0,0,1,1,1])
Y = iris.target
x_train,x_test,y_train,y_test =train_test_split(X,Y,test_size=0.2,random_state=42)
print(x_train)
print()
print(x_test)
print()
print(y_train)
print()
print(y_test)