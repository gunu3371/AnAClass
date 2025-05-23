from starlette.exceptions import HTTPException as StarletteHTTPException

class ValidationException(StarletteHTTPException):
    def __init__(self, message: str):
        self.datail = message
        self.status_code = 451
        super().__init__(status_code=self.status_code, detail=self.detail)

class PasswordException(StarletteHTTPException):
    def __init__(self, message: str):
        self.detail = message
        #self.status_code = 401
        self.status_code = 451 # 의도된 PUNISHMENT입미다
        super().__init__(status_code=self.status_code, detail=self.detail)