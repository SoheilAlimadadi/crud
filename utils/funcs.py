import os
import tomllib
from typing import Dict


def get_settings() -> Dict[str, str]:
    """
    Retrieve settings from a TOML configuration file.

    Returns a dictionary containing key-value pairs for the settings
    specified in the configuration file.

    Returns
    -------
    dict
        A dictionary containing key-value pairs for the settings in the
        configuration file.

    Raises
    ------
    IOError
        If the configuration file cannot be read.

    ValueError
        If the configuration file is invalid.

    Examples
    --------
    >>> settings = get_settings()
    >>> print(settings)
    {'host': 'localhost', 'port': '8080', 'debug': 'True'}
    """
    with open('settings.toml', 'rb') as settings_file:
        config = tomllib.load(settings_file)['settings']
    return config


def create_directories(base_dir: str, directories: list[tuple[str]]) -> None:
    """
    Creates a series of directories based on the input parameters.

    Args:
    - base_dir (str): The base directory in which the subdirectories will be created.
    - directories (list of tuples): A list of tuples where each tuple represents a subdirectory to create.
      The first element of each tuple is the name of the subdirectory, and the rest of the elements (if any)
      represent subdirectories within the previous directory.

    Example:
    base_dir = '/path/to/base'
    directories = [('logs',), ('logs', 'core')]
    create_directories(base_dir, directories)

    This will create the following directories:
    - /path/to/base/logs
    - /path/to/base/logs/core
    """
    for directory in directories:
        path = os.path.join(base_dir, *directory)
        if not os.path.exists(path):
            os.makedirs(path)
