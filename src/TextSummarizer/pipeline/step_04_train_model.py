"""
The data Transformation pipeline.
"""

from src.TextSummarizer.components.train_model import ModelTrainer
from src.TextSummarizer.config.config_manager import ConfigManager
from src.TextSummarizer.entity import entities
from src.TextSummarizer.logger import backend_logger


class ModelTrainerPipeline:
    """
    The data Transformation pipeline.
    """

    def run(self):
        """
        The main function of the train model pipeline.
        """
        backend_logger.info("Starting the train model pipeline.")
        config: ConfigManager = ConfigManager()
        train_model_config: entities.DataTransformationConfig = config.get_model_trainer_config()
        train_model = ModelTrainer(config=train_model_config)
        train_model.train()
        backend_logger.info("Finished the train model pipeline.")
