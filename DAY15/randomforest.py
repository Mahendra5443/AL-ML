from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,mean_absolute_error,mean_squared_error,r2_score)
rf = RandomForestClassifier(
    n_estimators=50,
    random_state=42
)
X,y = load_iris(return_X_y=True)
# print(X)
# print(y)
x_train, x_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42)
rf.fit(x_train, y_train)
pred = rf.predict(x_test)
print(pred)
print(accuracy_score(y_test, pred))