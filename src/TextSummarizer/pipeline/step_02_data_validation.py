"""
The data validation pipeline.
"""

from src.TextSummarizer.components.data_validation import DataValidation
from src.TextSummarizer.config.config_manager import ConfigManager
from src.TextSummarizer.entity import entities
from src.TextSummarizer.logger import backend_logger


class DataValidationPipeline:
    """
    The data validation pipeline.
    """

    def run(self):
        """
        The main function of the data validation pipeline.
        """
        backend_logger.info("Starting the data validation pipeline.")
        config: ConfigManager = ConfigManager()
        data_ingestion_config: entities.DataIngestionConfig = config.get_data_validation_config()
        data_ingestion = DataValidation(config=data_ingestion_config)
        data_ingestion.validate_all_files_exist()
        backend_logger.info("Finished the data validation pipeline.")
