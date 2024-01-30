from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

features_cols = [
    "bedrooms", "bathrooms", "sqft_living", "sqft_lot",
    "floors", "waterfront", "view", "condition",
    "sqft_above", "sqft_basement", "yr_built", "yr_renovated",
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Ensure fields are present and handle missing fields with a default value of 0
        features = [float(request.form.get(col, 0)) for col in features_cols]
        predicted_price = model.predict([features])[0]
        return render_template("index.html", predicted_price=f"The predicted price is ${predicted_price:.2f}")
    except ValueError:
        return render_template("index.html", error="Please enter valid values.")

if __name__ == "__main__":
    app.run(debug=True)
