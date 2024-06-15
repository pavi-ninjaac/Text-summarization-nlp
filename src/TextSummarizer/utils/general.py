"""
The functions used throughout the project is present here.
"""

import os
from pathlib import Path
from typing import Any

import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations

from src.TextSummarizer.logger import backend_logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read yaml file and return as Dictionary.

    :param path_to_yaml: Path to yaml file.
    :return: A ConfigBox dictionary object containing the the yaml file contents.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            backend_logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty.")
    except Exception as exp:
        raise exp


def create_directories(path_to_directories: list) -> None:
    """
    create list of directories.

    :params path_to_directories: list of path of directories.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        backend_logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the file size in KB.

    :param path: Path of the file.
    :returns: Size in KB.
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
