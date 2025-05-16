from fastapi import HTTPException

async def check_password(password):
    if password == "2025AnA":
        return "인증성공"
    else:
        raise HTTPException(status_code=401, detail="get out!!!!!!!!")