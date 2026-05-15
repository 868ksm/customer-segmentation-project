from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")

@app.route("/", methods=["GET", "POST"])
def index():
    cluster = None

    if request.method == "POST":
        age = float(request.form["age"])
        income = float(request.form["income"])
        score = float(request.form["score"])

        data = pd.DataFrame([[age, income, score]], columns=[
            "Age",
            "Annual_Income",
            "Spending_Score"
        ])

        scaled_data = scaler.transform(data)

        cluster = model.predict(scaled_data)[0]

    return render_template("index.html", cluster=cluster)

if __name__ == "__main__":
    app.run(debug=True)
