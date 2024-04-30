from typing import Optional

from pydantic import BaseModel, Field, validator


class Enrollment(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    cpf: str = Field(...,min_length=11, max_length=11)
    age: int = Field(..., gt=0)

    @validator("cpf")
    def cpf_must_be_numeric(cls, v, ):
        if not v.isdigit():
            raise ValueError("CPF must only contain digits")
        return v

class EnrollmentOut(BaseModel):
    id: str
    name: str
    cpf: str
    age: int
    enrollment_status: str
    error_message: Optional[str] = None
