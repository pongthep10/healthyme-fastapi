import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from src.shared.utils_helper import JsonHelper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("shinemon-san")

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

chatpify_database_ssm = os.getenv("chatpify_database_ssm")
chatpify_database_dict = JsonHelper.json_from_string(chatpify_database_ssm)

CHATPIFY_HOST = chatpify_database_dict.get("db_host")