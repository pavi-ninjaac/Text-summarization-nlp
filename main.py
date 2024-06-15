"""
The file which does the all work. Calling all the pipeline to do the training.
"""

from src.TextSummarizer.logger import backend_logger
from src.TextSummarizer.pipeline.step_01_data_ingestion import DataIngestionPipeline

stage_name: str = "Stage 1: Data Integration Stage"
line_msg: str = "="*100

try:
    backend_logger.info(line_msg)
    backend_logger.info(f"Stage {stage_name} started")
    DataIngestionPipeline().run()
    backend_logger.info(f"Stage {stage_name} completed.")
    backend_logger.info(line_msg)
except Exception as err:
    backend_logger.error(f"Data ingestion pipeline failed. Reason: {err}")
