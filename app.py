from flask import Flask, render_template, request
import pickle
import pandas as pd

# Load model bundle
with open("shopper_tree.pkl", "rb") as f:
    bundle = pickle.load(f)

model = bundle["model"]
encoders = bundle["encoders"]
feature_order = bundle["feature_order"]

app = Flask(__name__)

def preprocess(form_data):
    # Convert True/False strings to boolean
    sample = {
        k: (v if v not in ["True", "False"] else v == "True")
        for k, v in form_data.items()
    }

    df = pd.DataFrame([sample])

    # Encode categorical columns
    for col in df.columns:
        if col in encoders:
            df[col] = encoders[col].transform(df[col])

    # Match training column order
    df = df.reindex(columns=feature_order).fillna(0)

    return df


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        X_new = preprocess(request.form)
        pred = model.predict(X_new)

        # ✅ FIXED HERE (removed Revenue encoder issue)
        prediction = bool(pred[0])

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)