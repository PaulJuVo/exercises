import logging
from functools import wraps
import logging.config
# for handler in logging.root.handlers[:]:
#    logging.root.removeHandler(handler)


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        }
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "standard",
            "filename": "errors.log",
            "mode": "a",
        },
    },

    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    },
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)

