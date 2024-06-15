"""
All the class return types are present here.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass()
class DataIngestionConfig:
    """
    The return type of the data ingestion config function.
    """
    dataset_name: str
    arrow_dataset_dir: str


@dataclass()
class DataValidationConfig:
    """
    Return type of the data validation config function.
    """
    root_dir: str
    status_file: str
    all_required_folders: list


@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Return type of the data transformation config function.
    """
    root_dir: str
    data_path: str
    tokenizer_name: str


@dataclass(frozen=True)
class ModelTrainerConfig:
    """
    Return type of the model trainer config function.
    """
    root_dir: str
    data_path: str
    model_ckpt: str
    model_path: str
    tokenizer_path: str
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int


@dataclass(frozen=True)
class ModelEvaluationConfig:
    """
    Return type of the model evaluation config function.
    """
    root_dir: str
    data_path: str
    model_path: str
    tokenizer_path: str
    metric_file_name: str
