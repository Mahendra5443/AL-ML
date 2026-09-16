from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import pandas as pd
model = LogisticRegression()
df = pd.DataFrame({
    "hours":[1,2,3,4,5,6,7,8,9,10],
    "passed":[0,0,0,0,1,1,1,1,1,1]
})
X=df[["hours"]]
y = df["passed"]
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42)
model.fit(X_train,y_train)
prediction = model.predict(X_test)
accuracy = accuracy_score(y_test,prediction)
conf_matrix = confusion_matrix(y_test,prediction)
print(accuracy)
print(conf_matrix)
print(model.predict_proba(X_test))