from typing import Optional
from fastapi import APIRouter, Depends, Security, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.security import HTTPBearer
from src.infrastructure.repositories.htme_postgres.user_repository import UserRepository
from src.interfaces.serializers.authentication_serializer import TokenOut
from src.infrastructure.webserver.shared.authentication import authenticate_user, create_access_token
router = APIRouter()
security = HTTPBearer()

@router.post("/token", response_model=TokenOut)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.email, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if ACCESS_TOKEN_EXPIRE_MINUTES:
        ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
