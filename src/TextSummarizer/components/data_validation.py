import os

from src.TextSummarizer.entity import entities
from src.TextSummarizer.logger import backend_logger


class DataValidation:
    def __init__(self, config: entities.DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        """
        Check if all the required folders are present.
        """
        try:
            validation_status: bool | None = None

            all_folder = os.listdir(os.path.join("artifacts","data"))

            for folder in all_folder:
                print(folder)
                if folder not in self.config.all_required_folders:
                    validation_status = False
                    with open(self.config.status_file, "w") as f:
                        backend_logger.info("Writing the data validation status as False")
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status_file, "w") as f:
                        backend_logger.info("Writing the data validation status as True")
                        f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as exp:
            raise exp