# logging_utils.py
import logging


def setup_logging():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.info("Logging is configured!")
    return logger
