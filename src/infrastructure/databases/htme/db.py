from src.infrastructure.databases.htme.config import database

class DbManager:
    async def __init__(self):
        self.db = await database.connect()
        return
    def __enter__(self):
        return self.db

    async def __exit__(self, exc_type, exc_value, traceback):
        await self.db.commit()
        self.db.close()
