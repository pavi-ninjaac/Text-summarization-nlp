"""
The file which does the all work. Calling all the pipeline to do the training.
"""

from src.TextSummarizer.logger import backend_logger
from src.TextSummarizer.pipeline.step_01_data_ingestion import DataIngestionPipeline
from src.TextSummarizer.pipeline.step_02_data_validation import DataValidationPipeline
from src.TextSummarizer.pipeline.step_03_data_transformation import (
    DataTransformationPipeline,
)
from src.TextSummarizer.pipeline.step_04_train_model import ModelTrainerPipeline
from src.TextSummarizer.pipeline.step_05_model_evaluation import ModelEvaluationPipeline

stage_name_01: str = "Stage 1: Data Integration Stage"
stage_name_02: str = "Stage 2: Data Validation Stage"
stage_name_03: str = "Stage 3: Data Transformation Stage"
stage_name_04: str = "Stage 4: Model training Stage"
stage_name_05: str = "Stage 5: Model Evaluation Stage"


line_msg: str = "="*100

try:
    backend_logger.info(line_msg)
    backend_logger.info(f"Stage {stage_name_01} started")
    DataIngestionPipeline().run()
    backend_logger.info(f"Stage {stage_name_01} completed.")
    backend_logger.info(line_msg)
except Exception as err:
    backend_logger.error(f"Data ingestion pipeline failed. Reason: {err}")


try:
    backend_logger.info(line_msg)
    backend_logger.info(f"Stage {stage_name_02} started")
    DataValidationPipeline().run()
    backend_logger.info(f"Stage {stage_name_02} completed.")
    backend_logger.info(line_msg)
except Exception as err:
    backend_logger.error(f"Data validation pipeline failed. Reason: {err}")


try:
    backend_logger.info(line_msg)
    backend_logger.info(f"Stage {stage_name_03} started")
    DataTransformationPipeline().run()
    backend_logger.info(f"Stage {stage_name_03} completed.")
    backend_logger.info(line_msg)
except Exception as err:
    backend_logger.error(f"Data Transformation pipeline failed. Reason: {err}")


# For the device limitations issues, i have trained the model on online and stored the model in huggingface profile.
# We can skip the training and model evaluation steps while running locally.


try:
    backend_logger.info(line_msg)
    backend_logger.info(f"Stage {stage_name_04} started")
    ModelTrainerPipeline().run()
    backend_logger.info(f"Stage {stage_name_04} completed.")
    backend_logger.info(line_msg)
except Exception as err:
    backend_logger.error(f"Data data training pipeline failed. Reason: {err}")


try:
    backend_logger.info(line_msg)
    backend_logger.info(f"Stage {stage_name_05} started")
    ModelEvaluationPipeline().run()
    backend_logger.info(f"Stage {stage_name_05} completed.")
    backend_logger.info(line_msg)
except Exception as err:
    backend_logger.error(f"Model evaluation pipeline failed. Reason: {err}")
