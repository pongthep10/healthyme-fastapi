try:
    import unzip_requirements
except ImportError:
    pass
from settings import logger
from src.infrastructure.webserver.root import app
from mangum import Mangum
import uvicorn

handler = Mangum(app)
if __name__ == '__main__':
    uvicorn.run(app)