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

from src.TextSummarizer.logging import backend_logger


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
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
