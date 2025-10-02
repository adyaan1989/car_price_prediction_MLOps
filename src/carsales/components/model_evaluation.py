# import os
# import pandas as pd
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# from urllib.parse import urlparse
# import mlflow
# import mlflow.sklearn
# import numpy as np
# import joblib
# from carsales.entity.config_entity import ModelEvaluationConfig
# from carsales.utils.common import save_json
# from pathlib import Path
# import matplotlib.pyplot as plt
# import seaborn as sns
# from dotenv import load_dotenv

# #Load environment variables from .env file
# load_dotenv()

# os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLFLOW_TRACKING_USERNAME")
# os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")

# class ModelEvaluation:
#     def __init__(self, config: ModelEvaluationConfig):
#         self.config = config
    
#     def eval_metrics(self, actual, pred):
#         actual = np.ravel(actual)
#         pred = np.ravel(pred)
#         r2 = r2_score(actual, pred)
#         rmse = np.sqrt(mean_squared_error(actual, pred))
#         mae = mean_absolute_error(actual, pred)
#         return r2, rmse, mae

#     # def eval_metrics(self, actual, pred):
#     #     r2 = r2_score(actual, pred)
#     #     rmse = np.sqrt(mean_squared_error(actual, pred))
#     #     mae = mean_absolute_error(actual, pred)
#     #     return r2, rmse, mae
    
#     def log_into_mlflow(self):
#         x_test = pd.read_csv(self.config.x_test_data_path)
#         y_test = pd.read_csv(self.config.y_test_data_path)
#         model = joblib.load(self.config.model_path)
#         print("x_test shape:", x_test.shape)
#         print("y_test shape:", y_test.shape)


#         mlflow.set_registry_uri(self.config.mlflow_uri)
#         tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        

#         with mlflow.start_run(run_name="Model Evaluation"):
            
#             predict_price = model.predict(x_test)
#             print("predict_price shape:", predict_price.shape)

#             (r2, rmse, mae) = self.eval_metrics(y_test, predict_price)

#             # Saving metrics as local
#             scores = {"r2":r2, "rmse":rmse, "mae":mae}
#             save_json(path=Path(self.config.metric_file_name), data=scores)
            
#             # Log parameters and metrics
#             mlflow.log_params(self.config.all_params)
#             mlflow.log_metrics(scores)
            
#             mlflow.log_metric("r2", r2)
#             mlflow.log_metric("rmse", rmse)
#             mlflow.log_metric("mae", mae)

#              # Log evaluation plots
#             # 1. Actual vs Predicted
#             plt.figure(figsize=(6, 4))
#             sns.scatterplot(x=y_test.values.flatten(), y=predict_price.flatten())
#             plt.xlabel("Actual")
#             plt.ylabel("Predicted")
#             plt.title("Actual vs Predicted")
#             plt.savefig("actual_vs_predicted.png")
#             mlflow.log_artifact("actual_vs_predicted.png")

#             # 2. Residuals
#             residuals = y_test.values.flatten() - predict_price.flatten()
#             plt.figure(figsize=(6, 4))
#             sns.histplot(residuals, bins=30, kde=True)
#             plt.xlabel("Residuals")
#             plt.title("Residual Distribution")
#             plt.savefig("residuals_plot.png")
#             mlflow.log_artifact("residuals_plot.png")
                
#             # Model registry does not work with file store
#             if tracking_url_type_store != "file":
                
#                 # Register the model
#                 # There are other ways to use the Model Registry, which depends on the use case,
#                 # please refer to the doc for more information:
#                 # https://mlflow.org/docs/latest/model-registry.html#api-workflow
#                 mlflow.sklearn.log_model(model,"model", registered_model_name="ElasticnetModel")
#                 #mlflow.sklearn.log_model(model,"model", registered_model_name="sk-learn-random-forest-reg-model")
#             else:
#                 mlflow.sklearn.log_model(model, "model")
                



import os
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from dotenv import load_dotenv
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn

from carsales.entity.config_entity import ModelEvaluationConfig
from carsales.utils.common import save_json

# Load environment variables from .env file
load_dotenv()

# Set MLFLOW credentials (safer to do this right after loading .env)
os.environ["MLFLOW_TRACKING_USERNAME"] = os.getenv("MLFLOW_TRACKING_USERNAME")
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self, actual, pred):
        """Evaluate R2, RMSE, and MAE."""
        actual = np.ravel(actual)
        pred = np.ravel(pred)
        r2 = r2_score(actual, pred)
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        return r2, rmse, mae
    
    def log_into_mlflow(self):
        # Load test data
        x_test = pd.read_csv(self.config.x_test_data_path)
        y_test = pd.read_csv(self.config.y_test_data_path)
        model = joblib.load(self.config.model_path)

        print(f"x_test shape: {x_test.shape}")
        print(f"y_test shape: {y_test.shape}")

        # Get predictions
        predict_price = model.predict(x_test)

        
        print(f"predict_price shape: {predict_price.shape}")

        # Set MLflow tracking
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run(run_name="Model Evaluation"):

            # Evaluate model
            r2, rmse, mae = self.eval_metrics(y_test, predict_price)

            # Save metrics locally
            scores = {"r2": r2, "rmse": rmse, "mae": mae}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Log to MLflow
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)

            # Plot 1: Actual vs Predicted
            plt.figure(figsize=(6, 4))
            sns.scatterplot(x=y_test.values.flatten(), y=predict_price.flatten())
            plt.xlabel("Actual")
            plt.ylabel("Predicted")
            plt.title("Actual vs Predicted")
            plt.savefig("actual_vs_predicted.png")
            mlflow.log_artifact("actual_vs_predicted.png")

            # Plot 2: Residual distribution
            residuals = y_test.values.flatten() - predict_price.flatten()
            plt.figure(figsize=(6, 4))
            sns.histplot(residuals, bins=30, kde=True)
            plt.xlabel("Residuals")
            plt.title("Residual Distribution")
            plt.savefig("residuals_plot.png")
            mlflow.log_artifact("residuals_plot.png")

            # Log model
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")
