from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
accuracy_score,mean_absolute_error,mean_squared_error,r2_score)
import numpy as np
# Load Dataset

iris = load_iris()

X = iris.data

Y = iris.target

# Train-Test Split

x_train, x_test, y_train, y_test = train_test_split(X, Y,test_size=0.2,random_state=42)
# Create Model

model = LogisticRegression(max_iter=200)


# Train Model

model.fit(x_train, y_train)
# Predict
predictions = model.predict(x_test)
# Print Predictions
print("Predictions:")

print(predictions)
print("\nActual Values:")
print(y_test)
# Accuracy
accuracy = accuracy_score(y_test, predictions)
print("\nAccuracy:", accuracy)
# Coefficients
print("\nCoefficients:")
print(model.coef_)
# Intercept
print("\nIntercept:")
print(model.intercept_)
# MAE (Mean Absolute Error)
mae = mean_absolute_error(y_test, predictions)
print("\nMAE:", mae)
# MSE (Mean Squared Error)
mse = mean_squared_error(y_test, predictions)
print("MSE:", mse)
# RMSE (Root Mean Squared Error)
rmse = np.sqrt(mse)
print("RMSE:", rmse)

# R² Score
r2 = r2_score(y_test, predictions)
print("R² Score:", r2)
# Predict New Sample
new_flower = [[5.1, 3.5, 1.4, 0.2]]
predicted_class = model.predict(new_flower)
print("\nPredicted Class:", predicted_class[0])
print("Predicted Species:", iris.target_names[predicted_class[0]])