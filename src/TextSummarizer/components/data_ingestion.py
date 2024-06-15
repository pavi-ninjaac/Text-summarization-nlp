import os

from datasets import load_dataset

from src.TextSummarizer.entity import entities


class DataIngestionComponent:
    """
    A Class which is responsible for data ingestion.
    """

    def __init__(self, config: entities.DataIngestionConfig) -> None:
        self.config = config

    def save_dataset(self):
        """
        Load the dataset.
        """
        # if the dataset is already loaded then don't call it.
        if os.path.exists(self.config.arrow_dataset_dir):
            return

        test_dataset = load_dataset(self.config.dataset_name)
        test_dataset.save_to_disk(self.config.arrow_dataset_dir)
