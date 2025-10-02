import os
import urllib.request as request
import zipfile
from carsales.logging import logger
from carsales.utils.common import get_size
from carsales.entity.config_entity import ModelTrainerConfig
from pathlib import Path
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        x_train = pd.read_csv(self.config.x_train_data_path)
        y_train = pd.read_csv(self.config.x_train_data_path)
        x_test = pd.read_csv(self.config.x_test_data_path)
        y_test = pd.read_csv(self.config.y_test_data_path)
        


        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(x_train, y_train)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
                    
