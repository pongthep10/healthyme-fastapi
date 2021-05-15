from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from src.infrastructure.webserver.api.v1.main import router
from src.infrastructure.webserver.api.v1.endpoints.user_endpoint import router as user_router
# from src.infrastructure.webserver.api.v1.endpoints.ws import router as ws_router
# from src.infrastructure.webserver.api.v1.endpoints.dashboard import router as dashboard_router
from settings import SECRET_KEY, ROOT_PATH, logger


app = FastAPI(
    title="Healthy-me",
    description="htme",
    version="1.0.0",
    root_path=ROOT_PATH,
)

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


class Settings(BaseModel):
    authjwt_secret_key: str = SECRET_KEY
    authjwt_denylist_enabled: bool = False
    authjwt_denylist_token_checks: set = {"access", "refresh"}
    # Configure application to store and get JWT from cookies
    # authjwt_token_location: set = {"cookies"}
    # Only allow JWT cookies to be sent over https
    # authjwt_cookie_secure: bool = False
    # Enable csrf double submit protection. default is True
    # authjwt_cookie_csrf_protect: bool = True
    # Change to 'lax' in production to make your website more secure from CSRF Attacks,
    # default is None
    # authjwt_cookie_samesite: str = 'strict'


@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    # status_code: int = exc.status_code
    status_code: int = 401
    message: str = exc.message
    logger.error(f"JWT Token exception: {message}")

    return JSONResponse(
        status_code=status_code,
        content={"detail": exc.message}
    )


app.include_router(router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1/user")
app.include_router(user_router, prefix="/api/v1/user")
# app.include_router(ws_router, prefix="/api/v1/ws")


@app.get("/")
async def htme():
    return "Please go the a proper path directory"
