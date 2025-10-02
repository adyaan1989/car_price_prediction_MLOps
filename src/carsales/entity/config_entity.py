from dataclasses import dataclass
from pathlib import Path
from typing import List

## Data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

## Data Validation
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: Path 
    all_schema: dict

# data transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    numerical_features: List[str]
    categorical_features: List[str]
    outlier_features: List[str]
    drop_columns: List[str]
    target_column: str


@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    x_train_data_path: Path
    y_train_data_path: Path
    x_test_data_path: Path
    y_test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str 
