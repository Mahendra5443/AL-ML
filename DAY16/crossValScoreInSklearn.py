import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split

# Data
df = pd.DataFrame(
    {
        "age": [20, 22, 25, 28, 30, 35, 40, 45, 50, 55, 60, 65, 70, 72, 75],
        "income": [20, 22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 85, 90],
        "purchased": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    }
)

X = df[["age", "income"]]
y = df["purchased"]

# 1. Pehle Train aur Test split karein
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(n_estimators=100, random_state=42)

# 2. StratifiedKFold use karein taaki har fold me 0 aur 1 ka ratio sahi rahe
cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

# 3. Cross Validation SIRF X_train par chalayein
scores = cross_val_score(model, X_train, y_train, cv=cv, scoring="accuracy")

print("Fold Scores:", scores)
print("CV Mean Accuracy:", scores.mean())

# 4. Final Evaluation on Test Set
model.fit(X_train, y_train)
test_acc = model.score(X_test, y_test)
print("Unseen Test Accuracy:", test_acc)