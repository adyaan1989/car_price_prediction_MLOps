import joblib
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        # Load trained model and preprocessor
        self.model = joblib.load(Path("dataStore/model_trainer/model.joblib"))
        self.preprocessor = joblib.load(Path("dataStore/data_transformation/preprocessor.pkl"))

        # Define the feature column order (very important)
        self.columns = [
            "make", "model", "year", "mileage", "engine_hp", "transmission", "fuel_type",
            "drivetrain", "body_type", "exterior_color", "interior_color", "owner_count",
            "accident_history", "seller_type", "condition", "trim", "vehicle_age",
            "mileage_per_year", "brand_popularity"
        ]

    def predict(self, data):
        """
        Predict car price using trained model and preprocessor.

        Args:
            data (np.array): shape (1, 19), raw input from form

        Returns:
            float: predicted price (original scale)
        """
        # Convert input to DataFrame
        input_df = pd.DataFrame(data, columns=self.columns)

        # Apply preprocessing
        transformed_input = self.preprocessor.transform(input_df)

        # Predict (model was trained on log1p(price))
        pred_log = self.model.predict(transformed_input)

        # Inverse log transform
        pred_price = np.expm1(pred_log)

        return np.round(pred_price[0], 2)
