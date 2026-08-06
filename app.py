from flask_cors import CORS
from flask import jsonify
from flask import Flask, render_template, request
import pandas as pd
import joblib
import numpy as np
import shap
import os
from core.model_engine import HybridFraudModel

app = Flask(__name__)
CORS(app)
# --- 1. GLOBAL INITIALIZATION ---
try:
    print("⏳ Loading models... this may take a moment.")
    
    if not os.path.exists('models/scaler.pkl'):
        raise FileNotFoundError("Run 'train_main.py' first to generate model files!")

    scaler = joblib.load('models/scaler.pkl')
    xgb_loaded = joblib.load('models/xgboost_model.pkl')
    iso_loaded = joblib.load('models/iso_forest.pkl')

    engine = HybridFraudModel()
    engine.xgb_model = xgb_loaded
    engine.iso_forest = iso_loaded

    explainer = shap.TreeExplainer(xgb_loaded)
    print("✅ System Ready: Models and XAI Explainer loaded.")

except Exception as e:
    print(f"❌ CRITICAL ERROR: {e}")
    engine = None
    scaler = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not engine:
        return jsonify({"error": "System not ready"})

    try:
        raw_data = request.json   # 🔥 CHANGE HERE (JSON instead of form)
        input_df = pd.DataFrame([raw_data])

        for i in range(1, 29):
            col = f'V{i}'
            if col not in input_df.columns:
                input_df[col] = 0.0

        if 'Amount' not in input_df.columns:
            input_df['Amount'] = 0.0
        if 'Time' not in input_df.columns:
            input_df['Time'] = 0.0

        input_df = input_df.astype(float)

        amount_val = input_df['Amount'].values.reshape(-1,1)
        time_val = input_df['Time'].values.reshape(-1,1)

        input_df['scaled_amount'] = scaler.transform(amount_val)
        input_df['scaled_time'] = scaler.transform(time_val)

        feature_order = [f'V{i}' for i in range(1,29)] + ['scaled_amount','scaled_time']
        features = input_df[feature_order]

        risk_score = engine.get_risk_score(features)

        return jsonify({
            "risk_score": float(risk_score),
            "status": "fraud" if risk_score > 75 else "legit"
        })

    except Exception as e:
        return jsonify({"error": str(e)})
# 🔥 ADD THIS RIGHT BELOW /predict ROUTE

@app.route("/sample/<type>", methods=["GET"])
def get_sample(type):

    try:
        df = pd.read_csv("data/creditcard.csv") # Make sure this file exists in same folder

        if type == "legit":
            row = df[df["Class"] == 0].sample(1).iloc[0]
        elif type == "fraud":
            row = df[df["Class"] == 1].sample(1).iloc[0]
        elif type == "random":
            row = df.sample(1).iloc[0]   # 🔥 Random from full dataset
        else:
            return jsonify({"error": "Invalid type"}), 400

        response = {
            "pca": [float(row[f"V{i}"]) for i in range(1,29)],
            "amount": float(row["Amount"]),
            "time": float(row["Time"])
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)