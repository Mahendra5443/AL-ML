from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
model = LinearRegression()
iris = load_iris()
X = iris.data
Y = iris.target
x_train,x_test,y_train,y_test =train_test_split(X,Y,test_size=0.2,random_state=42)
model.fit(x_train,y_train)

predictions = model.predict(x_test)
print(predictions)
print(y_test)
print(model.coef_)
print(model.intercept_)

# MEA mean absolute error 1/n sumOf(y-ymean)

#MSE mean squred error

#RMSE root mean squred error

#R^2

