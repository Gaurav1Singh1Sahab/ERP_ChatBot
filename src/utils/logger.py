import logging
import logging.config
from pathlib import Path

def setup_logger(name: str):
    path = Path(__file__).parent.parent / "configs/logging.conf"
    logging.config.fileConfig(path)
    return logging.getLogger(name)
