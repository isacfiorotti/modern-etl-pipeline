import logging
from functools import wraps
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            logger = logging.getLogger(func.__module__)
            logger.info(f"Enter: {func.__name__}")
            logger.info(f"Args:{args}")
            logger.info(f"Kwargs:{kwargs}")
            start_time = time.time()
            func(*args, **kwargs)
            end_time = start_time - time.time()
            logger.info(f"Exit: {func.__name__}")
            logger.info(f"Runtime: {end_time:.4f}s")
        except Exception as e:
            logger.error(f"Function: {func.__name__} \n {e}", exc_info=True)
            raise
    return wrapper