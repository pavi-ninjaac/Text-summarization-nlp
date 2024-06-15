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
