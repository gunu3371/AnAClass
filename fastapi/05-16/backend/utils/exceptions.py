class ValidationException(Exception):
    """Custom exception for validation errors."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.status_code = 422
        self.error_type = "Validation Error"
        self.error_message = message