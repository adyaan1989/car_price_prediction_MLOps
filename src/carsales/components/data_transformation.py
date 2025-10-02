import os
import numpy as np
import urllib.request as request
import zipfile
from carsales.logging import logger
from carsales.utils.common import get_size
from carsales.entity.config_entity import DataTransformationConfig
from pathlib import Path
from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, PowerTransformer, LabelEncoder, OrdinalEncoder, RobustScaler
from sklearn.impute import SimpleImputer
import category_encoders as ce
import joblib




class DataTransformation:
    def __init__(
            self, config: DataTransformationConfig):
        
        """
        Initialize the DataTransformation class with config.
        """
        self.config = config

    def load_data(self) -> pd.DataFrame:
        """
        Load and clean the dataset.
        """
        df = pd.read_csv(self.config.data_path)
        logger.info(f"Data loaded from {self.config.data_path}")

        #df.drop(columns=["accident_history","engine_hp"], axis=1, inplace=True)
        
        df["price"] = np.log1p(df["price"])
        return df

    def split_data(self, df: pd.DataFrame) -> None:
        
        """
        Splits the data into train/test and stores them.
        """
         
        X = df.drop(columns=["price"], axis=1)
        y = df["price"]

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)
        
        logger.info(f"Train shape: {self.X_train.shape}")
        logger.info(f"Test shape: {self.X_test.shape}")
        logger.debug(f"Train sample:\n{self.X_train.head()}")

    def build_preprocessor(self) -> ColumnTransformer:
        """
        Builds a preprocessing pipeline for numerical, categorical, and outlier features.
        """

        drop_cols = set(self.config.drop_columns)

        numerical = [col for col in self.config.numerical_features if col not in drop_cols]
        categorical = [col for col in self.config.categorical_features if col not in drop_cols]
        outliers = [col for col in self.config.outlier_features if col not in drop_cols]

        
        # Create Column Transformer with 3 types of transformers
        numeric_feature_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ("scaler", RobustScaler())
        ])

        categorical_features_pipeline = Pipeline(steps=[
            ('SimpleImputer', SimpleImputer(strategy='most_frequent')),
            ('target_encoder', ce.TargetEncoder())
        ])

        outlier_features_pipeline = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('transformer', PowerTransformer(standardize=True))
        ])

        preprocessor = ColumnTransformer([
            ("Numerical features Pipeline", numeric_feature_pipeline, numerical),
            ("categorical features pipeline",categorical_features_pipeline, categorical),
            ("Outlier Features Pipeline", outlier_features_pipeline, outliers)
        ])

        logger.info("Preprocessor pipeline created.")
        return preprocessor

    def transform_and_save(self, preprocessor: ColumnTransformer) -> None:
        """
        Applies the transformation, saves processed datasets and preprocessor.
        """

        # Transform
        train_x = preprocessor.fit_transform(self.X_train, self.y_train)
        test_x = preprocessor.transform(self.X_test)

        # Convert to DataFrames (columns optional — you can use get_feature_names_out if supported)
        train_x_df = pd.DataFrame(train_x)
        test_x_df = pd.DataFrame(test_x)

        # Save transformed data
        root = self.config.root_dir
        os.makedirs(root, exist_ok=True)

        train_x_df.to_csv(os.path.join(root, "x_train.csv"), index=False)
        self.y_train.to_csv(os.path.join(root, "y_train.csv"), index=False)
        test_x_df.to_csv(os.path.join(root, "x_test.csv"), index=False)
        self.y_test.to_csv(os.path.join(root, "y_test.csv"), index=False)

        logger.info("Transformed datasets saved successfully.")
        # Save preprocessor
        joblib.dump(preprocessor, os.path.join(root, "preprocessor.pkl"))
        logger.info("Preprocessor object saved successfully.")


    def run(self) -> None:
        """
        Executes the complete transformation pipeline.
        """
        logger.info("Starting data transformation...")

        df = self.load_data()
        self.split_data(df)
        preprocessor = self.build_preprocessor()
        self.transform_and_save(preprocessor)

        logger.info("Data transformation completed.")


        

        
    