import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

df = pd.DataFrame({
    "age": [20, 22, 25, 27, 30, 45, 48, 50, 52, 55],
    "income": [20, 22, 25, 28, 30, 70, 75, 80, 85, 90]
})

X = df[["age", "income"]]
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

kmeans.fit(X_scaled)
labels = kmeans.labels_
print(kmeans.cluster_centers_)
print(labels)
print(kmeans.inertia_)  
