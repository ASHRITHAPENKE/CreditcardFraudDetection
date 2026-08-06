import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def fit_and_save(self, df, path='models/scaler.pkl'):
        # Scale 'Amount' and 'Time'
        df['scaled_amount'] = self.scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
        df['scaled_time'] = self.scaler.fit_transform(df['Time'].values.reshape(-1, 1))
        
        # Drop original columns and keep the PCA ones (V1-V28)
        df.drop(['Time', 'Amount'], axis=1, inplace=True)
        
        # Save the scaler for use in the Flask app later
        joblib.dump(self.scaler, path)
        return df

    def transform_single(self, input_data, scaler_path='models/scaler.pkl'):
        # Used for real-time web input
        scaler = joblib.load(scaler_path)
        # Apply scaling logic to single input...
        pass