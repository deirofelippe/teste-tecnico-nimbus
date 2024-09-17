import os, time
from loguru import logger
from datetime import datetime

os.environ["TZ"] = "America/Sao_Paulo"
time.tzset()

now = datetime.now().strftime("%Y%m%d")
format = "{time:YYYY-MM-DD  HH:mm:ss} | {level} | {message} "

logger.remove(0)
logger.add(
    f"/app/aplicacao-1/logs/log_{now}.log",
    rotation="1 days",
    retention="7 days",
    format=format,
)
