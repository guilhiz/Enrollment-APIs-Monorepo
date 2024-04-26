from pydantic import BaseModel

class AgeGroup(BaseModel):
    id: int
    min_age: int
    max_age: int
