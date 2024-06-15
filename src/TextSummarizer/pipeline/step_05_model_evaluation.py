"""
The data Transformation pipeline.
"""

from src.TextSummarizer.components.model_evaluation import ModelEvaluation
from src.TextSummarizer.config.config_manager import ConfigManager
from src.TextSummarizer.entity import entities
from src.TextSummarizer.logger import backend_logger


class ModelEvaluationPipeline:
    """
    The model evaluation pipeline.
    """

    def run(self):
        """
        The main function of the model evaluation pipeline.
        """
        backend_logger.info("Starting the  model evaluation pipeline.")
        config = ConfigManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()
        backend_logger.info("Finished the model evaluation pipeline.")
