from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from router import router as api_router
from utils.exceptions import *

app = FastAPI(
    title="20250516",
    description="집가고싶다",
    version="69.74"
)

app.include_router(api_router)

@app.exception_handler(ValidationException)
async def validation_exception_handler(request: Request, exc: ValidationException):
    return JSONResponse(
        status_code=451,
        content={
            "error": {
                "message": "!!FBI WARNING!!",
                "detail": str(exc.message)
            }
        }
    )