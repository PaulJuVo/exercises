import logging
from functools import wraps

def log_calls(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(logging.INFO,f"→ {func.__name__} gestartet mit args={args}, kwargs={kwargs}")
            try:
                result = func(*args, **kwargs)
                logger.log(logging.INFO,f"← {func.__name__} beendet, Ergebnis={result}")
                return result
            except Exception as e:
                logger.log(logging.ERROR,f"Fehler in {func.__name__}: {e}")
                raise
        return wrapper
    return decorator