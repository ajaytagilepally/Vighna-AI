import logging
import os

log_level = os.getenv("LOG_LEVEL", "info").upper()
logger = logging.getLogger("vighna_ai")
logger.setLevel(log_level)

# Console handler
handler = logging.StreamHandler()
handler.setLevel(log_level)

# Formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)

logger.addHandler(handler)
