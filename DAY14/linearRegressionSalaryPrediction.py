from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (mean_absolute_error,mean_squared_error,r2_score,accuracy_score, confusion_matrix)
import pandas as pd
import numpy as np
# Perform:
# Train/test split
# Linear Regression
# Training prediction
# Testing prediction
# MAE
# RMSE
# R²
# Print coefficients
# Print intercept
df = pd.DataFrame({
"experience": [1,2,3,4,5,6,7,8,9,10,11,12],
"age": [21,22,23,24,25,26,27,28,29,30,31,32],
"projects": [1,2,2,3,4,4,5,6,6,7,8,9],
"salary": [25000,28000,31000,35000,
39000,43000,48000,52000,
57000,62000,68000,75000]})
X=df[["experience","age","projects"]]
y = df["salary"]
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42)
model = LinearRegression()
model.fit(X_train,y_train)
prediction = model.predict(X_test)
mae = mean_absolute_error(y_test, prediction)
rmse = np.sqrt(mean_squared_error(y_test, prediction))
r2 = r2_score(y_test, prediction)
print("\nCoefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef}")
print("\nIntercept:")
print(model.intercept_)