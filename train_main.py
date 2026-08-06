import pandas as pd
from sklearn.model_selection import train_test_split
from core.preprocessor import DataPreprocessor
from core.model_engine import HybridFraudModel
import os

# 1. Setup Directories
os.makedirs('models', exist_ok=True)
os.makedirs('data', exist_ok=True)

def run_training():
    print(" Starting Hybrid ML Training...")

    # 2. Load Dataset
    # Make sure your creditcard.csv is in the 'data/' folder
    data_path = 'data/creditcard.csv'
    if not os.path.exists(data_path):
        print(f"❌ Error: {data_path} not found. Please add the Kaggle dataset.")
        return

    df = pd.read_csv(data_path)

    # 3. Preprocessing
    preprocessor = DataPreprocessor()
    df_cleaned = preprocessor.fit_and_save(df)
    
    X = df_cleaned.drop('Class', axis=1)
    y = df_cleaned['Class']

    # 4. Split Data (Stratified to handle imbalance)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 5. Hybrid Model Training
    engine = HybridFraudModel()
    engine.train(X_train, y_train)
    
    print("✅ Training Complete! Models saved in /models/")
    print(f"   - Scaler saved.")
    print(f"   - XGBoost (Supervised) saved.")
    print(f"   - Isolation Forest (Anomaly) saved.")

if __name__ == "__main__":
    run_training()