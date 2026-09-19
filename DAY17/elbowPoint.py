from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
scaler = StandardScaler()
df = pd.DataFrame({
    "age": [20, 22, 25, 27, 30, 45, 48, 50, 52, 55],
    "income": [20, 22, 25, 28, 30, 70, 75, 80, 85, 90]
})

X = df[["age", "income"]]

X_scaled = scaler.fit_transform(X)

inertias = []

for k in range(1, 11):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)

    inertias.append(model.inertia_)
plt.plot(range(1,11),inertias,marker="o")
plt.title('elbow Method')
plt.ylabel('Inertia')
plt.xlabel('No. of Clusters')
plt.show()
print(inertias)
