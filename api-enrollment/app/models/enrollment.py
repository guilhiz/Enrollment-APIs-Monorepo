from pydantic import BaseModel, Field


class Enrollment(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    cpf: str = Field(min_length=11, max_length=14)
    age: int = Field(gt=0)
    enrollment_status: str = "active"


class EnrollmentOut(BaseModel):
    id: str
    name: str
    cpf: str
    age: int
    enrollment_status: str
