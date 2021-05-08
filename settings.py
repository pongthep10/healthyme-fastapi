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
CHATPIFY_DATABASE = chatpify_database_dict.get("db_database")
CHATPIFY_USERNAME = chatpify_database_dict.get("db_user")
CHATPIFY_PASSWORD = chatpify_database_dict.get("db_password")
CHATPIFY_PORT = 5432

CHATPIFY_MESSAGE_ARN = os.getenv('chatpify_message_arn')
IKKYU_SAN_SYSTEM_AMPLIFY_ENDPOINT = os.getenv('IKKYU_SAN_SYSTEM_AMPLIFY_ENDPOINT')
IKKYU_SAN_SYSTEM_AMPLIFY_API_KEY = os.getenv('IKKYU_SAN_SYSTEM_AMPLIFY_API_KEY')
IKKYU_SAN_SYSTEM_FB_CUSTOMER_ENDPOINT = os.getenv('IKKYU_SAN_SYSTEM_FB_CUSTOMER_ENDPOINT')
IKKYU_SAN_SYSTEM_FB_CUSTOMER_API_KEY = os.getenv('IKKYU_SAN_SYSTEM_FB_CUSTOMER_API_KEY')

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = os.getenv("secret_key")
ALGORITHM = os.getenv("algorithm")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("access_token_expire_minutes"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("refresh_token_expire_days"))

REDIS_HOST = os.getenv("redis_host")
REDIS_PASSWORD = os.getenv("redis_password")
REDIS_PORT = int(os.getenv("redis_port"))
REDIS_DB = int(os.getenv("redis_db"))
REDIS_CHANNEL_WS = os.getenv("redis_channel_ws")

NSQAI_URI = os.getenv("NSQAI_URI")
NSQAI_USER = os.getenv("NSQAI_USER")
NSQAI_PASSWORD = os.getenv("NSQAI_PASSWORD")
NSQAI_PORT = int(os.getenv("NSQAI_PORT"))
NSQAI_DATABASE = os.getenv("NSQAI_DATABASE")

MESSAGING_CENTER_SERVICE_ENDPOINT = os.getenv("MESSAGING_CENTER_SERVICE_ENDPOINT")
MESSAGING_CENTER_KEY = os.getenv("MESSAGING_CENTER_KEY")

S3_ACCESS_KEY_ID = os.getenv("S3_ACCESS_KEY_ID")
S3_SECRET_ACCESS_KEY = os.getenv("S3_SECRET_ACCESS_KEY")
S3_REGION = os.getenv("S3_REGION")
S3_MARKETING_SC = os.getenv("S3_MARKETING_SC")
S3_TAG = os.getenv("S3_TAG")

SNS_CONTINUE_WITH_BOT = os.getenv("SNS_CONTINUE_WITH_BOT_ARN")

SHINEMON_SAN_X_API_KEY = os.getenv("SHINEMON_SAN_X_API_KEY")
SHINEMON_SAN_API_KEY_NAME = os.getenv("SHINEMON_SAN_API_KEY_NAME")

PRODUCT_CATALOG_V2_ENDPOINT = os.getenv("PRODUCT_CATALOG_V2_ENDPOINT")
PRODUCT_CATALOG_V2_API_KEY = os.getenv("PRODUCT_CATALOG_V2_API_KEY")

CHATPIFY_EXPRESS_ENDPOINT_API = os.getenv("CHATPIFY_EXPRESS_ENDPOINT_API")
CHATPIFY_EXPRESS_KEY = os.getenv("CHATPIFY_EXPRESS_KEY")

PAYMENY_STATE_X_API_KEY = os.getenv("PAYMENY_STATE_X_API_KEY")

FB_APP_ID = os.getenv("FB_APP_ID")
FB_APP_SECRET = os.getenv("FB_APP_SECRET")
