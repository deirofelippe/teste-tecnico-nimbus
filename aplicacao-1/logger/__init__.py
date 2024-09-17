import sys
from loguru import logger

format = (
    "<white>{time:YYYY/MM/DD HH:mm:ss}</white> | <green>{level}</green> | {message}"
)

logger.remove(0)
logger.add(
    sys.stdout,
    format=format,
)
