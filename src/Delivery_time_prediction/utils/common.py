import os
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import List
from Delivery_time_predection.logger import logger

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty or cannot be loaded.

    Returns:
        ConfigBox: ConfigBox containing the YAML content.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file '{path_to_yaml}' loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise ValueError(f"Error loading YAML file '{path_to_yaml}': {e}")


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create a list of directories.

    Args:
        path_to_directories (list): List of paths of directories.
        verbose (bool, optional): Print log messages for created directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file in KB.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
