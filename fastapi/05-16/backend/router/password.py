from fastapi import APIRouter, Path, Header
from service.password import check_password

from pydantic import BaseModel

from typing import Optional

router = APIRouter()

class AnAModel(BaseModel):
    result: Optional[str] = None
    message: Optional[str] = None

class PaswordField_Input(BaseModel):
    password: str = Path(..., min_length=1, max_length=128, title="Password", description="Password Field")
    secret : str = Header(..., title="Secret Token", description="Secret Token")

@router.post("/auth/{password}", response_model=AnAModel)
async def Huawei_safe_auth(
    model: PaswordField_Input,
    ):
    if model.secret is None or model.secret != "2025ANA":
        return "Invalid Token"
    result = await check_password(model.password) 
    return AnAModel(result=result, message="Success")