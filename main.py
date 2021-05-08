from settings import logger
# try:
#     if event.get('source') == 'serverless-plugin-warmup':
#         logger.info('WarmUP - Lambda is warm!')
#         return True
# except:
#     pass
from src.infrastructure.webserver.root import app

from mangum import Mangum
import uvicorn
handler = Mangum(app)
if __name__ == '__main__':
    uvicorn.run(app)