from fastapi import HTTPException
from utils.exceptions import *

async def check_password(password):
    if password == "2025AnA":
        return "REWARD를 주마 \n" \
        "REWARD=은교님은 사실xx과출신이란다"
    else:
        #raise HTTPException(status_code=401, detail="get out!!!!!!!!")
        raise PasswordException(message="get out!!!!!!!!")