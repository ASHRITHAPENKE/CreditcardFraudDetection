import xgboost as xgb
from sklearn.ensemble import IsolationForest
import joblib

class HybridFraudModel:
    def __init__(self):
        self.xgb_model = xgb.XGBClassifier(
            n_estimators=100, 
            max_depth=6, 
            learning_rate=0.1, 
            scale_pos_weight=580 # Handles imbalance
        )
        self.iso_forest = IsolationForest(contamination=0.01, random_state=42)

    def train(self, X_train, y_train):
        # 1. Train Supervised XGBoost
        self.xgb_model.fit(X_train, y_train)
        
        # 2. Train Unsupervised Isolation Forest (On normal data only)
        self.iso_forest.fit(X_train[y_train == 0])
        
        # Save models
        joblib.dump(self.xgb_model, 'models/xgboost_model.pkl')
        joblib.dump(self.iso_forest, 'models/iso_forest.pkl')

    def get_risk_score(self, input_df):
        # Probability from XGBoost
        xgb_prob = self.xgb_model.predict_proba(input_df)[:, 1][0]
        
        # Anomaly score from IsoForest (normalized to 0-1 range)
        # IsoForest returns -1 for anomaly, 1 for normal
        iso_score = self.iso_forest.decision_function(input_df)[0]
        norm_iso_score = 1 - (iso_score + 0.5) # Simple normalization logic
        
        # Hybrid weighted score
        final_risk = (0.7 * xgb_prob) + (0.3 * norm_iso_score)
        return round(final_risk * 100, 2)