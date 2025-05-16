from pydantic import BaseModel

class Student(BaseModel):
    name: str
    student_id: int
    department: str
    grede: int
    club: str
