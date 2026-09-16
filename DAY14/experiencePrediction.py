import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (mean_absolute_error,mean_squared_error,r2_score)
# Create DataFrame
df = pd.DataFrame({
"experience": [1,2,3,4,5,6,7,8,9,10,11,12],
"age": [21,22,23,24,25,26,27,28,29,30,31,32],
"projects": [1,2,2,3,4,4,5,6,6,7,8,9],
"salary": [25000,28000,31000,35000,39000,43000,48000,52000,57000,62000,68000,75000]
})
# Features and Target
X = df[["experience", "age", "projects"]]
y = df["salary"]
# 1. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2,random_state=42)
# 2. Linear Regression
model = LinearRegression()
# Train Model
model.fit(X_train, y_train)
# 3. Training Prediction
train_predictions = model.predict(X_train)
# 4. Testing Prediction
test_predictions = model.predict(X_test)
print("Training Predictions:")
print(train_predictions)
print("\nTesting Predictions:")
print(test_predictions)
# 5. MAE
mae = mean_absolute_error(y_test, test_predictions)
print("\nMAE:", mae)
# 6. RMSE
rmse = np.sqrt(mean_squared_error(y_test, test_predictions))
print("RMSE:", rmse)
# 7. R² Score
r2 = r2_score(y_test, test_predictions)
print("R² Score:", r2)
# 8. Coefficients
print("\nCoefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef}")
# 9. Intercept
print("\nIntercept:")
print(model.intercept_)
# 10. Predict Salary for New Employee
new_employee = [[13, 33, 10]]
predicted_salary = model.predict(new_employee)
print("\nPredicted Salary:")
print(predicted_salary[0])