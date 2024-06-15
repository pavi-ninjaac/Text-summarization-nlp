"""
Configuration manager to get and set all the configuration.
"""

from pathlib import Path

from box import ConfigBox

from src.TextSummarizer.constants import file_path
from src.TextSummarizer.entity import entities
from src.TextSummarizer.utils.general import create_directories, read_yaml


# Create a config manager.
class ConfigManager:
    """
    Class to manage the configuration files.
    """

    def __init__(self) -> None:
        self.config: ConfigBox = read_yaml(Path(file_path.CONFIG_FILE_PATH))
        self.params: ConfigBox = read_yaml(Path(file_path.PARAMS_FILE_PATH))

        create_directories(path_to_directories=[self.config.artifacts_root])

    def get_data_ingestion_config(self) -> entities.DataIngestionConfig:
        """
        Get the config which is needed to download the data files.
        """
        config: ConfigBox = self.config.data_ingestion

        data_ingestion_config: entities.DataIngestionConfig = entities.DataIngestionConfig(
            dataset_name=config.dataset_name,
            arrow_dataset_dir=config.arrow_dataset_dir,
        )

        return data_ingestion_config

    def get_data_validation_config(self) -> entities.DataValidationConfig:
        """
        Get the config which is needed to validate the data files.
        """
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = entities.DataValidationConfig(
            root_dir=config.root_dir,
            status_file=config.status_file,
            all_required_folders=config.all_required_folders,
        )

        return data_validation_config