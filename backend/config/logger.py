from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | {message}"
)

logger.add(
    "backend/logs/app.log",
    rotation="5 MB",
    retention="10 days",
    level="DEBUG"
)

app_logger = logger