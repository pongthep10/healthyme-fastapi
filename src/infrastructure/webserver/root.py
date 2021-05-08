from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from src.infrastructure.webserver.api.v1.main import router
from src.infrastructure.webserver.api.v1.endpoints.ws import router as ws_router
from src.infrastructure.webserver.api.v1.endpoints.dashboard import router as dashboard_router
from settings import SECRET_KEY, logger


app = FastAPI(
    title="Shinemon-san",
    description="Chat Management System.",
    version="1.0.24",
)

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "http://shinemon-san.dev.nsq.cloud",
    "https://shinemon-san.dev.nsq.cloud",
    "http://shinemon-san.service.nsq.cloud",
    "https://shinemon-san.service.nsq.cloud",
    "http://melvinify-ui.dev.nsq.cloud",
    "https://melvinify-ui.dev.nsq.cloud",
    "http://lvh.me:3000",
    "https://lvh.me:3000",
    "https://melvinify.dev.nsq.cloud",
    "http://melvinify.dev.nsq.cloud",
    "https://shinemon-san-api-staging.nsq.cloud",
    "https://shinemon-san-api.nsq.cloud",
    "https://shinemon-san-ws-staging.nsq.cloud",
    "ws://shinemon-san-ws-staging.nsq.cloud",
    "wss://shinemon-san-ws-staging.nsq.cloud",
    "ws://shinemon-san-ws.dev.nsq.cloud",
    "wss://shinemon-san-ws.dev.nsq.cloud",
    "ws://shinemon-san-ws.service.nsq.cloud",
    "wss://shinemon-san-ws.service.nsq.cloud",
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
app.include_router(ws_router, prefix="/api/v1/ws")
app.include_router(dashboard_router, prefix="/api/v1/dashboard")


@app.get("/")
async def shinemon_san():
    return {"name": "shinemon-san"}
