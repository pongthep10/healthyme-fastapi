# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from aiopg.sa import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
from settings import DB_HTME_HOST, DB_HTME_PORT, DB_HTME_DB, DB_HTME_USER, DB_HTME_PASSWORD

DATABASE_URL = f"postgresql://{DB_HTME_USER}:{DB_HTME_PASSWORD}@{DB_HTME_HOST}:{DB_HTME_PORT}/{DB_HTME_DB}" #+asyncpg

# engine = create_async_engine(DATABASE_URL, future=True, echo=True)
# # engine = create_engine(user=DB_HTME_USER,
# #                              database=DB_HTME_DB,
# #                              host=DB_HTME_HOST,
# #                              password=DB_HTME_PASSWORD,
# #                              port=DB_HTME_PORT)

# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, class_=AsyncSession)
# Base = declarative_base()

import databases
import sqlalchemy
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL#, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)