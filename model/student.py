from pydantic import BaseModel

class student_dto(BaseModel):
    full_name:str
    student_id:str
    email:str
    age:int
    course:str