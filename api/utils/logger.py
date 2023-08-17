import logging

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

def setup_logger():
    """
    Configure the logging settings using the predefined LOGGING_CONFIG.
    """
    logging.config.dictConfig(LOGGING_CONFIG)

def get_logger():
    """
    Get a logger instance for your application.
    
    Returns:
        logger : A logger instance configured with the specified settings.
    """
    # Create a logger instance for your application
    logger = logging.getLogger(__name__)

    return logger