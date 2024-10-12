import sys
import os, time
from loguru import logger
from datetime import datetime

log_type = os.environ.get("LOG_TYPE")

os.environ["TZ"] = "America/Sao_Paulo"
time.tzset()

now = datetime.now().strftime("%Y%m%d")
format = "{time:YYYY-MM-DD  HH:mm:ss} | {level} | {message} "

logger.remove(0)

if log_type == "file":
    logger.add(
        f"/app/aplicacao-1/logs/log_{now}.log",
        rotation="1 days",
        retention="7 days",
        format=format,
    )
else:
    logger.add(sys.stdout, colorize=True, format=format)
