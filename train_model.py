import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib

df = pd.read_csv("customer_segmentation.csv")

X = df[["Age", "Annual_Income", "Spending_Score"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = KMeans(n_clusters=3, random_state=42)
model.fit(X_scaled)

df["Cluster"] = model.labels_

joblib.dump(model, "model.joblib")
joblib.dump(scaler, "scaler.joblib")

df.to_csv("clustered_customers.csv", index=False)

print("Model trained successfully!")
print("Clusters created successfully!")
