import logging
from rich.logging import RichHandler
from typing import Optional
from pathlib import Path

def setup_logger(name: str, log_file: Optional[str] = None, level: int = logging.INFO) -> logging.Logger:
    """Configures both file and console handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()

    # Console handler
    console_handler = RichHandler(rich_tracebacks=True)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    if log_file:
        file_path = Path(log_file)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def get_logger(name: str) -> logging.Logger:
    """Returns configured logger."""
    return logging.getLogger(name)
