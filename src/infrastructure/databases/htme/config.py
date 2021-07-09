try:
    import unzip_requirements
except ImportError:
    pass
from settings import DB_HTME_HOST, DB_HTME_PORT, DB_HTME_DB, DB_HTME_USER, DB_HTME_PASSWORD

DATABASE_URL = f"postgresql://{DB_HTME_USER}:{DB_HTME_PASSWORD}@{DB_HTME_HOST}:{DB_HTME_PORT}/{DB_HTME_DB}" #+asyncpg

import databases
import sqlalchemy
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL#, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)