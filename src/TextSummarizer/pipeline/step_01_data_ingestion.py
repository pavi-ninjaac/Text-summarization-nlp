"""
The data ingestion pipeline.
"""

from src.TextSummarizer.components.data_ingestion import DataIngestionComponent
from src.TextSummarizer.config.config_manager import ConfigManager
from src.TextSummarizer.entity import entities
from src.TextSummarizer.logger import backend_logger


class DataIngestionPipeline:
    """
    The data ingestion pipeline.
    """

    def run(self):
        """
        The main function of the data ingestion pipeline.
        """
        backend_logger.info("Starting the data ingestion pipeline.")
        config: ConfigManager = ConfigManager()
        data_ingestion_config: entities.DataIngestionConfig = config.get_data_ingestion_config()
        data_ingestion = DataIngestionComponent(config=data_ingestion_config)
        data_ingestion.save_dataset()
        backend_logger.info("Finished the data ingestion pipeline.")
