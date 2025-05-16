from fastapi import APIRouter, Header, HTTPException
from schema.student import Student
from service.student import register as reg
from utils.digits_sum import find_digits_sum
from utils.exceptions import ValidationException
router = APIRouter()

@router.post("/register")
async def register(student: Student, validation_code: int = Header(...)):
    if find_digits_sum(student.student_id * (student.grede)) != validation_code:
        ValidationException("Invalid validation code")
    return reg(student)
