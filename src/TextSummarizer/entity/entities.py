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
