from typing import Optional
from fastapi import APIRouter, Depends, Security, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.security import HTTPBearer
from src.infrastructure.repositories.htme_postgres.user_repository import UserRepository
from src.interfaces.serializers.authentication_serializer import TokenOut
from src.shared.exception import HtmeError
from src.infrastructure.webserver.shared.authentication import authenticate_user, create_access_token
from datetime import datetime, timedelta
from settings import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM


router = APIRouter()
security = HTTPBearer()

@router.post("/token", response_model=TokenOut)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        user_entity = await authenticate_user(form_data.username, form_data.password)
        if not user_entity:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user_entity.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HtmeError as e:
        raise HTTPException(status_code=401, detail=e.message)
    except Exception as e:
        print(traceback.format_exc())
        print(e)
        raise HTTPException(status_code=500, detail="Somethig went worng")
    return created_customer_entity