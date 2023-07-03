import tomllib
import logging.config
import logging
from .base import (
    BASE_DIR,
    config
)
from utils.funcs import create_directories

DIRECTORIES = config['log']['LOG_DIRS']

create_directories(BASE_DIR, DIRECTORIES)

with open('config/log/logging.toml', mode='rb') as config_file:
    log_conf_dict = tomllib.load(config_file)
    logging.config.dictConfig(log_conf_dict)

coreLogger = logging.getLogger('core')
