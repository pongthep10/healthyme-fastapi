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
ROOT_PATH = os.getenv("ROOT_PATH")
DB_HTME_HOST = os.getenv("DB_HTME_HOST")
DB_HTME_PORT = os.getenv("DB_HTME_PORT")
DB_HTME_DB = os.getenv("DB_HTME_DB")
DB_HTME_USER = os.getenv("DB_HTME_USER")
DB_HTME_PASSWORD = os.getenv("DB_HTME_PASSWORD")