# Decorator para computar o tempo de execução:
from datetime import datetime
from functools import wraps

from loguru import logger


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        elapsed_time = end_time - start_time
        logger.info(f"Function '{func.__name__}' executed in {elapsed_time}")
        return result

    return wrapper
