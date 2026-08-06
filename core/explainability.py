import shap
import joblib

def get_explanation(input_data):
    model = joblib.load('models/xgboost_model.pkl')
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(input_data)
    
    # Return features that contributed most to the risk
    return shap_values