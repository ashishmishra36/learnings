import logging
from datetime import datetime

from configs.config import TestData


def generate_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        log_file_name = datetime.now().strftime('%d%m%Y%H%M%S')
        file_handler = logging.FileHandler(TestData.LOG_FILE_PATH+log_file_name+'.log', mode='a')
        # define a format for logging
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
