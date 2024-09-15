import sys
from loguru import logger

format = (
    "<white>{time:DD/MM/YYYY HH:mm:ss}</white> | <green>{level}</green> | {message}"
)

logger.add(
    sys.stdout,
    format=format,
    colorize=True,
)
