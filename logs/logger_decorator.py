import logging
from functools import wraps

logger = logging.getLogger(__name__)

def log_calls(level=logging.INFO):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(level, f"→ {func.__name__} gestartet mit args={args}, kwargs={kwargs}")
            try:
                result = func(*args, **kwargs)
                logger.log(level, f"← {func.__name__} beendet, Ergebnis={result}")
                return result
            except Exception as e:
                logger.exception(f"Fehler in {func.__name__}: {e}")
                raise
        return wrapper
    return decorator