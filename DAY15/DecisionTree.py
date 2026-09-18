import pandas as pd
df = pd.DataFrame({
    "age": [22, 25, 28, 35, 40, 45, 50, 55, 60, 65],
    "income": [25, 30, 35, 45, 50, 60, 70, 80, 90, 100],
    "purchased": [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
})
X = df[["age", "income"]]
y = df["purchased"]
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=42)
tree1 = DecisionTreeClassifier(max_depth=2, random_state=42)
DecisionTreeClassifier(min_samples_split=10)
DecisionTreeClassifier(min_samples_leaf=5)
model.fit(X, y)
pred = model.predict(X)
print(pred)
print(model.feature_importances_)