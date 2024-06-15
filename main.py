"""
The file which does the all work. Calling all the pipeline to do the training.
"""

from src.TextSummarizer.logger import backend_logger
from src.TextSummarizer.pipeline.step_01_data_ingestion import DataIngestionPipeline
from src.TextSummarizer.pipeline.step_02_data_validation import DataValidationPipeline
from src.TextSummarizer.pipeline.step_03_data_transformation import (
    DataTransformationPipeline,
)

stage_name_01: str = "Stage 1: Data Integration Stage"
stage_name_02: str = "Stage 2: Data Validation Stage"
stage_name_03: str = "Stage 3: Data Transformation Stage"


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
