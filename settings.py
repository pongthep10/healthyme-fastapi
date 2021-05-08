import os
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('htme')
logger.setLevel(logging.INFO)
env_path = Path(".") / ".env"

try:
    from dotenv import load_dotenv
    load_dotenv(dotenv_path=env_path)
except Exception as e:
    logger.error(e)
    pass


load_dotenv(dotenv_path=env_path)

SECRET_KEY = os.getenv("SECRET_KEY")
