"""
The data Transformation pipeline.
"""

from src.TextSummarizer.components.data_transformation import DataTransformation
from src.TextSummarizer.config.config_manager import ConfigManager
from src.TextSummarizer.entity import entities
from src.TextSummarizer.logger import backend_logger


class DataTransformationPipeline:
    """
    The data Transformation pipeline.
    """

    def run(self):
        """
        The main function of the data Transformation pipeline.
        """
        backend_logger.info("Starting the data Transformation pipeline.")
        config: ConfigManager = ConfigManager()
        data_transformation_config: entities.DataTransformationConfig = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
        backend_logger.info("Finished the data Transformation pipeline.")
