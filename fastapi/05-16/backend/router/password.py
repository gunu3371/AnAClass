from fastapi import APIRouter, Path, Header
from service.password import check_password

router = APIRouter()

@router.post("/auth/{password}")
async def Huawei_safe_auth(
    password: str = Path(..., min_length=1, max_length=15),
    secret_token: str = Header(...)
    ):
    if secret_token is None or secret_token != "SARD_IS_TOP":
        return "Invalid Token"
    return await check_password(password)