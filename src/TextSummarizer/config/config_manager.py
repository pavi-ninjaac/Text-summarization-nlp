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

    def get_data_transformation_config(self) -> entities.DataTransformationConfig:
        """
        Get teh data transformation configurations.
        """
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = entities.DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config

    def get_model_trainer_config(self) -> entities.ModelTrainerConfig:
        """
        Get the configuration which is needed to train the model.
        """
        config = self.config.model_trainer
        params = self.params.TrainingArguments

        create_directories([config.root_dir])

        model_trainer_config = entities.ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path= config.model_path,
            tokenizer_path= config.tokenizer_path,
            model_ckpt = config.model_ckpt,
            num_train_epochs = params.num_train_epochs,
            warmup_steps = params.warmup_steps,
            per_device_train_batch_size = params.per_device_train_batch_size,
            weight_decay = params.weight_decay,
            logging_steps = params.logging_steps,
            evaluation_strategy = params.evaluation_strategy,
            eval_steps = params.evaluation_strategy,
            save_steps = params.save_steps,
            gradient_accumulation_steps = params.gradient_accumulation_steps
        )

        return model_trainer_config

    def get_model_evaluation_config(self) -> entities.ModelEvaluationConfig:
        """
        Get the model evaluation configuration.
        """
        config = self.config.model_evaluation

        create_directories([config.root_dir])

        model_evaluation_config = entities.ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path = config.model_path,
            tokenizer_path = config.tokenizer_path,
            metric_file_name = config.metric_file_name

        )

        return model_evaluation_config
