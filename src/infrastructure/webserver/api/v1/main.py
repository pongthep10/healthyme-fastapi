import traceback
from fastapi import APIRouter, Depends, Security, HTTPException, status
from fastapi.security import HTTPBearer
from fastapi.security.api_key import APIKeyHeader
# from fastapi.concurrency import run_in_threadpool
from fastapi_jwt_auth import AuthJWT
from typing import List, Optional

router = APIRouter()
security = HTTPBearer()

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/users")
async def get_users():
    return {"message": "Get Users!"}