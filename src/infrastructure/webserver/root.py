import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from src.infrastructure.webserver.api.v1.main import router
from src.infrastructure.webserver.api.v1.endpoints.user_endpoint import router as user_router
from settings import SECRET_KEY, ROOT_PATH, logger
from src.infrastructure.databases.htme.config import database

IS_LOCAL = os.environ.get('IS_LOCAL') == 'true'
print('IS_LOCAL', IS_LOCAL)
app = FastAPI(
    title="Healthy-me",
    description="htme",
    version="1.0.0",
    root_path=ROOT_PATH if not IS_LOCAL else ROOT_PATH,
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1/user")
