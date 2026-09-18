import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,precision_score,f1_score,recall_score
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

acc=[]
pre =[]
recall =[]
f1 =[]
kvalue =range(1,12)
for i in kvalue:
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train_scaled, y_train)
    pred = knn.predict(X_test_scaled)
    acc.append(accuracy_score(y_test, pred))
    pre.append(precision_score(y_test, pred))
    f1.append(f1_score(y_test, pred))
    recall.append(recall_score(y_test, pred))
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# 1. Accuracy Graph
axes[0, 0].plot(kvalue, acc, color="blue", marker="o")
axes[0, 0].set_title("Accuracy vs K-Value")
axes[0, 0].set_xlabel("K-Value")
axes[0, 0].set_ylabel("Score")
axes[0, 0].set_xticks(kvalue)
axes[0, 0].grid(True)

# 2. Precision Graph
axes[0, 1].plot(kvalue, pre, color="green", marker="s")
axes[0, 1].set_title("Precision vs K-Value")
axes[0, 1].set_xlabel("K-Value")
axes[0, 1].set_ylabel("Score")
axes[0, 1].set_xticks(kvalue)
axes[0, 1].grid(True)

# 3. Recall Graph
axes[1, 0].plot(kvalue, recall, color="orange", marker="^")
axes[1, 0].set_title("Recall vs K-Value")
axes[1, 0].set_xlabel("K-Value")
axes[1, 0].set_ylabel("Score")
axes[1, 0].set_xticks(kvalue)
axes[1, 0].grid(True)

# 4. F1-Score Graph
axes[1, 1].plot(kvalue, f1, color="red", marker="d")
axes[1, 1].set_title("F1-Score vs K-Value")
axes[1, 1].set_xlabel("K-Value")
axes[1, 1].set_ylabel("Score")
axes[1, 1].set_xticks(kvalue)
axes[1, 1].grid(True)

# Graphs ke beech jagah adjust karein aur display karein
plt.tight_layout()
plt.show()