import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.DataFrame({
"age": [20, 22, 25, 28, 30, 35, 40, 45, 50, 55,
60, 65, 70, 72, 75],
"income": [20, 22, 25, 30, 35, 40, 45, 50, 55, 60,
65, 70, 80, 85, 90],
"purchased": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1]
})

X = df[["age", "income"]]
y = df["purchased"]

X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.2,
random_state=42,
stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X_train_scaled, y_train)

pred = knn.predict(X_test_scaled)
print(pred)

print("Accuracy:", accuracy_score(y_test, pred))