import logging
import os.path
from datetime import datetime

from configs.config import TestData


def generate_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        log_file_name = datetime.now().strftime('%d%m%Y%H%M%S')
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_file_path = os.path.join(base_dir, '..', 'logs')
        file_handler = logging.FileHandler(log_file_path+log_file_name+'.log', mode='a')
        # define a format for logging
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
