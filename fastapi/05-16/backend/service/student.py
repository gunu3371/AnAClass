from schema.student import Student

async def register(regist: Student):
    return {
        "name": str(regist.name),
        "student_id": str(regist.student_id),
        "department": str(regist.department),
        "grede": str(regist.grede),
        "club": str(regist.club)
    }