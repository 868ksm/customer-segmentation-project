import joblib
import pandas as pd

model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

age = float(input("Enter age: "))
income = float(input("Enter annual income: "))
score = float(input("Enter spending score: "))

data = pd.DataFrame([[age, income, score]], columns=[
    "Age",
    "Annual_Income",
    "Spending_Score"
])

scaled_data = scaler.transform(data)

cluster = model.predict(scaled_data)[0]

print(f"Customer belongs to cluster: {cluster}")
