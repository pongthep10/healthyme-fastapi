from fastapi import APIRouter
router = APIRouter(
    prefix="",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/me")
async def get():
    return "ok"